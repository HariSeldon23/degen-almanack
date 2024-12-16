from manim import *
import numpy as np

class BancorCRRExplainer(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.2f}".format(num)

        # Create title and introduction
        title = Text("Bancor's Constant Reserve Ratio (CRR)", font_size=36)
        subtitle = Text("First Automated Market Maker", font_size=32, color=BLUE)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)

        # Initial explanation of CRR concept
        formula = Text("Price = Balance / (Supply × CRR)", font_size=28, color=GREEN)
        formula.next_to(subtitle, DOWN, buff=0.5)

        self.play(Write(formula))
        self.wait(1)

        # Create coordinate system for visualizing reserves and supply
        axes = Axes(
            x_range=[0, 20, 5],
            y_range=[0, 2000, 500],
            x_length=6,
            y_length=4,
            tips=False,
            axis_config={"include_numbers": False}
        ).shift(DOWN * 0.5 + LEFT * 2)

        x_label = Text("ETH Reserve", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Smart Tokens", font_size=24).next_to(axes.y_axis, UP)
        
        # Add axis labels
        x_values = VGroup()
        for x in [0, 5, 10, 15, 20]:
            label = Text(str(x), font_size=16)
            label.next_to(axes.c2p(x, 0), DOWN)
            x_values.add(label)

        y_values = VGroup()
        for y in [0, 500, 1000, 1500, 2000]:
            label = Text(str(y), font_size=16)
            label.next_to(axes.c2p(0, y), LEFT)
            y_values.add(label)

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(x_values),
            Write(y_values)
        )

        # Create initial state indicator
        initial_state = Dot(axes.c2p(10, 1000), color=BLUE)
        initial_label = Text("Initial State\n10 ETH, 1000 Tokens", font_size=20)
        initial_label.next_to(initial_state, RIGHT)

        self.play(
            Create(initial_state),
            Write(initial_label)
        )

        # Create CRR curve
        def crr_curve(x, crr=0.5):
            return 1000 * (x/10)**(1/crr)

        curve = axes.plot(
            crr_curve,
            x_range=[1, 20],
            color=YELLOW
        )
        curve_label = Text("CRR = 50%", font_size=20, color=YELLOW)
        curve_label.next_to(curve, UP)

        self.play(
            Create(curve),
            Write(curve_label)
        )

        # Show trade example
        buy_point = Dot(axes.c2p(11, crr_curve(11)), color=GREEN)
        buy_arrow = Arrow(
            initial_state.get_center(),
            buy_point.get_center(),
            color=GREEN
        )
        buy_label = Text("Buy 1 ETH", font_size=20, color=GREEN)
        buy_label.next_to(buy_arrow, UP)

        self.play(
            Create(buy_arrow),
            Create(buy_point),
            Write(buy_label)
        )

        # Show calculations
        calculations = VGroup(
            Text("Trade Example:", font_size=24),
            Text("Add 1 ETH to Reserve", font_size=20),
            Text("New Reserve: 11 ETH", font_size=20),
            Text("New Token Supply: 1048.81", font_size=20),
            Text("Maintains 50% CRR", font_size=20, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT)
        calculations.to_edge(RIGHT)

        self.play(Write(calculations))
        self.wait(1)

        # Show price impact
        price_impact = VGroup(
            Text("Price Impact:", font_size=24, color=RED),
            Text("Initial Price: $40/token", font_size=20),
            Text("New Price: $41.96/token", font_size=20),
            Text("4.9% Increase", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT)
        price_impact.next_to(calculations, DOWN)

        self.play(Write(price_impact))
        self.wait(1)

        # Clear for key points
        everything_else = VGroup(
            axes, x_label, y_label, x_values, y_values,
            initial_state, initial_label, curve, curve_label,
            buy_point, buy_arrow, buy_label, calculations,
            price_impact, formula
        )
        self.play(FadeOut(everything_else))

        # Key points about CRR
        notes = VGroup(
            Text("Key Features of CRR:", font_size=32, color=BLUE),
            Text("• Automatic price adjustment", font_size=28),
            Text("• Continuous liquidity at all prices", font_size=28),
            Text("• Dynamic token supply", font_size=28),
            Text("• Configurable reserve ratio", font_size=28),
            Text("• Mathematical price stability", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(2)

        # Show mechanism details
        self.play(FadeOut(notes))
        
        mechanism = VGroup(
            Text("How CRR Works:", font_size=32, color=BLUE),
            Text("1. Sets fixed reserve ratio", font_size=28),
            Text("2. Mints/burns tokens to maintain ratio", font_size=28),
            Text("3. Adjusts price based on reserve changes", font_size=28),
            Text("4. Ensures continuous liquidity", font_size=28),
            Text("5. Balances stability and efficiency", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        mechanism.move_to(ORIGIN)

        self.play(Write(mechanism))
        self.wait(3)

        # Add impact of different CRRs
        self.play(FadeOut(mechanism))
        
        crr_comparison = VGroup(
            Text("Impact of Different CRRs:", font_size=32, color=BLUE),
            Text("Low CRR (10-20%):", font_size=28),
            Text("• More price stability", font_size=24),
            Text("• Lower capital efficiency", font_size=24),
            Text("High CRR (80-100%):", font_size=28),
            Text("• More price volatility", font_size=24),
            Text("• Better capital efficiency", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        crr_comparison.move_to(ORIGIN)

        self.play(Write(crr_comparison))
        self.wait(3)