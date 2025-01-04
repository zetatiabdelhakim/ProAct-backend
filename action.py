import sqlite3

def add_levels(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    levels = [
        ("Your First Day as an Entrepreneur",
         """
        Situation:
        You've just officially started your entrepreneurial journey with a bold idea. You’re passionate, but the reality of running a business hits fast. You have to decide where to focus your energy first: should you build a detailed business plan, start networking to find early clients, or jump into product development? Each choice has risks—too much planning could delay action, while rushing into development without validation could backfire.

        Challenge:
        It’s your first day, and you can only focus on one priority. You need to decide how to make the most impact early on while keeping momentum. Should you map out every detail before taking action, or focus on smaller wins to build confidence?

        Text Box for Answer:
        What would you prioritize on your first day as an entrepreneur and why? How do you balance planning with taking action? Explain your strategy and how it would set the foundation for your business success.
         """,
         """
         On your first day, the key is to find a balance between planning and action. Start with a lean approach: outline a basic business model to clarify your value proposition, target market, and revenue streams, but avoid getting stuck in over-planning. Simultaneously, focus on small, impactful steps like networking with potential clients or validating your idea with early feedback. Early traction and real-world insights can help refine your plan as you move forward. Remember, progress often beats perfection in entrepreneurship.
         """),

        ("Face the Real Challenge",
         """
        Situation:
        Your startup has just launched its first product, but early feedback reveals a major flaw that could affect customer satisfaction. You have limited resources and fixing the issue could delay other important developments. On the other hand, ignoring the feedback could harm your reputation.

        Challenge:
        You must decide whether to pause your growth plans to fix the flaw or keep pushing forward with marketing while planning gradual improvements. How will you balance reputation, resources, and growth?

        Text Box for Answer:
        How would you approach this situation? Would you prioritize fixing the flaw immediately, or would you continue scaling with the risk of dissatisfied customers? Explain your decision and its impact on your startup's long-term vision.
         """,
         """
         Addressing the product flaw early is crucial for maintaining customer trust. Consider temporarily pausing marketing efforts to fix the major issue, as a damaged reputation can be harder to repair than a delayed launch. If resources are tight, prioritize the most critical fix that affects user experience the most. Communicate transparently with your customers about the improvements being made to maintain trust.
         """
         ),
        ("All About Timing",
         """
        Situation:
        You've developed an innovative app that solves a pressing problem. You're ready to launch, but a competitor has just released a similar product. If you wait to refine your product, you risk losing market attention. If you launch now, your app might lack some critical features.

        Challenge:
        Decide whether to launch immediately and risk falling short or delay for improvements and risk being overshadowed. Timing can make or break a startup—how will you handle it?

        Text Box for Answer:
        What would you do? Would you launch now or wait? Explain your reasoning and how you would ensure your decision helps your business thrive in the long run.
         """,
         """
         Launching too early with an incomplete product can damage your brand, while waiting too long can cost you market attention. Consider a "soft launch" with early adopters to gather feedback while continuing development. This way, you stay visible while refining your product. Timing is key, but balancing visibility with readiness is even more critical.
         """),
        ("Teamwork Makes the Dream Work",
         """
        Situation:
        You’ve assembled a diverse startup team, but conflicts have started to emerge around decision-making and work habits. Productivity is slowing, and team morale is dipping. You can step in as the leader, but that might create tension, or you can let the team figure it out, risking further delays.

        Challenge:
        How will you address the conflict? Would you intervene directly, set clearer collaboration guidelines, or take another approach? Balancing leadership and empowerment is key here.

        Text Box for Answer:
        What steps would you take to resolve team conflicts while keeping productivity high? Describe how you would foster collaboration and trust in your startup team.
         """,
         """
         Open communication is essential when conflicts arise in a team. Schedule a meeting where everyone can express their concerns openly. As the leader, guide the conversation towards finding collaborative solutions without taking sides. Establish clear roles and responsibilities while promoting a culture of mutual respect. Strong teamwork is built on transparency and shared goals.
         """),
        ("Not Deciding is Still a Decision",
         """
        Situation:
        You’ve just launched your startup and things are going well. However, to scale up quickly, you need more funding. An investor has approached you with an offer. They propose a large sum of money, but they want a significant share of your company in return. You’ve heard stories of entrepreneurs who regretted giving up too much control, but the investment could propel your startup to the next level.

        Challenge:
        You can either accept the offer and give away a portion of your business, or delay the decision in hopes of finding a better offer. But delaying means you risk losing the investor’s interest, and your startup might not grow as fast without the funding.

        Text Box for Answer:
        What would you do in this situation? Would you take the investment and give away part of your company, or would you wait for a better opportunity? How do you evaluate the long-term impact of waiting versus acting quickly?
         """,
         """
         When facing this situation, the key is balancing risk and opportunity. Evaluate the terms of the investment carefully—consider the percentage of equity being offered, the investor’s value beyond money (like mentorship or connections), and the long-term impact on decision-making power. If the offer feels too costly, explore alternative funding options such as grants, loans, or smaller investors. However, delaying indefinitely could stall your growth. The best approach is to gather enough information to make a timely, informed decision rather than avoiding it altogether.
         """),

        ("Deliver the Perfect Pitch",
         """
        Situation:
        You’ve been invited to pitch your startup at a major investor event. You have 3 minutes to make an impression. Your product is strong, but you're unsure whether to focus on storytelling, financial projections, or the uniqueness of your innovation.

        Challenge:
        You must craft a pitch that balances emotional impact with solid data. Choosing the wrong focus could make investors lose interest.

        Text Box for Answer:
        What would you emphasize in your pitch, and why? How would you structure your presentation to ensure maximum impact? Explain how your approach would win over investors.
         """,
         """
         A winning pitch balances storytelling and facts. Start with a compelling story that highlights the problem you’re solving, then back it with market size, revenue models, and growth potential. Keep it concise and focus on why your solution stands out. Close with a call to action for the investors, such as requesting a meeting or funding.
         """),

        ("Money Monie Moo",
         """
        Situation:
        Your startup is finally generating revenue, but you're struggling with cash flow. A big client has delayed payment, while operational costs keep piling up. You can either take a loan, cut team bonuses, or delay an important software upgrade.

        Challenge:
        Managing money is key to business survival. How would you balance short-term financial challenges without compromising team morale and product quality?

        Text Box for Answer:
        What financial decision would you make and why? Explain how you would keep the business stable while maintaining long-term goals.
         """,
         """
         When facing cash flow issues, avoid drastic measures that could harm team morale. Consider negotiating extended payment terms with suppliers or offering discounts for early payments from clients. If necessary, explore short-term financing options while clearly communicating your financial plan to the team. Keeping transparency builds trust during difficult times.
         """),

        ("The Grand Launch: Your Moment to Shine",
         """
        Situation:
        It’s launch day for your product, and you’ve invested heavily in marketing. Suddenly, a technical glitch affects your website, preventing users from signing up. Delaying the launch could damage your reputation, but proceeding with the glitch could frustrate early users.

        Challenge:
        Will you delay, or will you launch with the glitch while working on a fix? This moment could define how your audience perceives you.

        Text Box for Answer:
        What would you do? Would you delay the launch or go live despite the glitch? Explain your choice and how you would communicate with your audience.
         """,
         """
         If a glitch occurs during launch, prioritize quick damage control while maintaining transparency. Communicate the issue openly with your audience and offer a timeline for the fix. If the glitch doesn’t impact core features, you can proceed while working on the fix in the background. Honesty during setbacks can often strengthen customer loyalty.
         """),

        ("Every End is a Start",
         """
        Situation:
        Your first business idea didn't succeed, and you're closing down the startup. However, you’ve learned valuable lessons and built a solid network. You have the choice to start over with a new idea or take a break and reflect longer.

        Challenge:
        Failure isn't the end—it's a step forward. How would you use this experience to launch a stronger second venture?

        Text Box for Answer:
        What would you do next? Would you immediately start another business or take time to reflect? Explain how your past experiences would shape your next entrepreneurial move.
         """,
         """
         Failure is a powerful learning experience. Take time to reflect on what went wrong, whether it was market fit, team dynamics, or financial planning. Use these insights to refine your next business idea. Stay connected with the network you’ve built and seek mentorship. Remember, many successful entrepreneurs faced failure before their breakthrough.
         """),
        ("The Deep Dive, The Big Up",
         """
         Situation:
        You’ve been offered a chance to expand your startup into a new market with huge potential. However, entering this market requires a complete shift in your business model and additional resources. If it works, the rewards could be massive, but if it fails, you risk everything you’ve built.

        Challenge:
        Will you take the leap and pivot your business, or stay focused on your current market? How do you assess whether the risk is worth it?

        Text Box for Answer:
        Would you expand into the new market or focus on what’s working? Explain your decision and how you would manage risk while aiming for growth.
         """,
         """
         Before expanding into a new market, conduct thorough research on demand, competition, and costs. If the risk seems too high, consider testing with a pilot version or partnership instead of a full expansion. Balancing ambition with calculated risk is key to sustainable growth. Expand only when you can support both markets effectively.
         """)
    ]

    # Insert levels into the table
    for title, problem, solution in levels:
        cursor.execute("INSERT INTO Level (title, problem, solution) VALUES (?, ?, ?)", (title, problem, solution))

    conn.commit()
    conn.close()


def select_all_levels(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Level")
    levels = cursor.fetchall()

    for level in levels:
        print(f"Title: {level[0]}")
        print(f"Problem: {level[1]}")
        print(f"Solution: {level[2]}")
        print("-" * 50)

    conn.close()



db_path = 'instance/mydatabase.db'

# add_levels(db_path)
select_all_levels(db_path)