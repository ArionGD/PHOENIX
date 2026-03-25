from google import genai
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from portfolio.models import Holding
from decimal import Decimal
from django.utils import timezone
from datetime import timedelta
import markdown

# Configure Gemini Client (v2.0 SDK)
client = genai.Client(api_key=settings.GEMINI_API_KEY)

@login_required
def explain_market(request):
    # Initialize variables
    error = ""
    
    # Try to load from session first (for persistence across navigation)
    cached_data = request.session.get('last_ai_analysis', {})
    explanation_html = cached_data.get('explanation', '')
    timeline = cached_data.get('timeline', 'today')
    date_from = cached_data.get('date_from', '')
    date_to = cached_data.get('date_to', '')

    if request.method == "POST":
        timeline = request.POST.get('timeline', 'today')
        date_from = request.POST.get('date_from', '')
        date_to = request.POST.get('date_to', '')
        
        try:
            # Fetch user holdings
            holdings = Holding.objects.filter(user=request.user)
            
            if not holdings.exists():
                error = "You don't have any holdings to analyze. Please add some assets to your portfolio first."
            else:
                # Prepare portfolio summary for AI
                portfolio_summary = []
                total_value = Decimal('0.0')
                total_cost = Decimal('0.0')
                
                for h in holdings:
                    mv = h.market_value()
                    tc = h.total_cost()
                    total_value += mv
                    total_cost += tc
                    portfolio_summary.append(f"- {h.symbol} ({h.name}): {h.quantity} units, Current Price: ₹{h.current_price:,.2f}, Avg Buy Price: ₹{h.purchase_price:,.2f}, Type: {h.get_asset_type_display()}")

                total_pl = total_value - total_cost
                pl_pct = (total_pl / total_cost * 100) if total_cost > 0 else 0

                # Date anchoring
                now = timezone.now()
                today_str = now.strftime("%Y-%m-%d")
                yesterday_str = (now - timedelta(days=1)).strftime("%Y-%m-%d")

                # Determine period string
                if timeline == "today":
                    period_str = f"for today ({today_str})"
                elif timeline == "yesterday":
                    period_str = f"for yesterday ({yesterday_str})"
                elif timeline == "last_week":
                    period_str = f"over the last 7 days (ending {today_str})"
                elif timeline == "last_month":
                    period_str = f"over the last 30 days (ending {today_str})"
                else:
                    period_str = f"for the period from {date_from} to {date_to}"
                
                prompt = f"""
                CRITICAL INSTRUCTIONS:
                - TODAY'S DATE IS {today_str}.
                - You are a senior financial analyst at ALTAIR, a premium wealth management firm.
                - Analyze the portfolio holdings listed below specifically {period_str}.
                - Do NOT use dates from your training data (like 2024). Stick to the context of {today_str}.
                
                MY PORTFOLIO DATA ({today_str}):
                - Total Market Value: ₹{total_value:,.2f}
                - Total Investment: ₹{total_cost:,.2f}
                - Net Profit/Loss: ₹{total_pl:,.2f} ({pl_pct:.2f}%)
                
                HOLDINGS DETAIL:
                {chr(10).join(portfolio_summary)}
                
                REQUIRED SECTIONS (Use Markdown Headings):
                1. ## {timeline.replace('_', ' ').capitalize()} Performance Breakdown: Explain how these specific assets performed {period_str}.
                2. ## Current Market Drivers: Identify specific global and Indian market news/trends affecting these symbols.
                3. ## Critical Strategy: Forward-looking advice for this specific portfolio.
                
                Formatting: Use bold text, bullet points, and clean headers. Be specific to the symbols (e.g., RELIANCE, NIFTY_50).
                """

                # Call Gemini (v2 GenAI SDK)
                model_name = 'models/gemini-2.5-flash'
                try:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=prompt
                    )
                except Exception:
                    response = client.models.generate_content(
                        model='models/gemini-2.5-flash-lite-preview-09-2025',
                        contents=prompt
                    )
                
                # Convert Markdown to HTML
                explanation_html = markdown.markdown(response.text, extensions=['extra', 'nl2br'])
                
                # PERSIST TO SESSION: Save the analysis so it stays when navigating back
                request.session['last_ai_analysis'] = {
                    'explanation': explanation_html,
                    'timeline': timeline,
                    'date_from': date_from,
                    'date_to': date_to,
                    'generated_at': now.isoformat()
                }
            
        except Exception as e:
            error = f"Error generating explanation: {str(e)}"

    return render(request, 'analysis/explain.html', {
        'explanation': explanation_html,
        'error': error,
        'timeline': timeline,
        'date_from': date_from,
        'date_to': date_to
    })
