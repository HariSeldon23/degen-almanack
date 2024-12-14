from manim import *
import numpy as np

class CurveStableSwap(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.0f}".format(num)

        # Helper function for StableSwap curve
        def get_y(x, A):
            # Simplified 2-token StableSwap implementation
            # A is the amplification coefficient
            n = 2  # number of tokens
            D = 2_000_000  # Total depth (1M + 1M)
            
            # Calculate y using the invariant
            c = (D ** (n + 1)) / (n ** n * A)
            b = D - (x * n)
            
            # Solve quadratic equation
            try:
                y = (-b + np.sqrt(b*b + 4*c)) / 2
                return min(2_000_000, max(0, y))  # Clamp values
            except:
                return 0

        # Create title and formulas
        title = Text("Curve StableSwap Formula", font_size=36)
        subtitle = Text("An∑xᵢ + D = An·D + D/n·∑(1/xᵢ)", font_size=32, color=BLUE)
        explanation = Text("Combines constant sum and constant product", font_size=28, color=GREEN)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)
        explanation.next_to(subtitle, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(Write(explanation))
        self.wait(1)

        # Initial state - two stablecoins at $1
        initial_state = VGroup(
            Text("Initial Pool State:", font_size=24),
            Text("USDC: 1,000,000", font_size=24),
            Text("USDT: 1,000,000", font_size=24),
            Text("Both tokens ≈ $1", font_size=24),
            Text("Amplification (A) = 100", font_size=24, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT)
        initial_state.to_edge(LEFT).shift(UP)

        self.play(Write(initial_state))
        self.wait(1)

        # Create three coordinate systems for different A values
        axes_group = VGroup()
        curves_group = VGroup()
        labels_group = VGroup()

        A_values = [1, 100, 1000]
        curve_colors = [BLUE, GREEN, RED]
        
        for i, (A, color) in enumerate(zip(A_values, curve_colors)):
            # Create axis
            axes = Axes(
                x_range=[0, 2_000_000, 500_000],
                y_range=[0, 2_000_000, 500_000],
                x_length=3,
                y_length=3,
                tips=False,
                axis_config={"include_numbers": False}
            ).shift(DOWN * 0.5 + RIGHT * (i * 4 - 4))
            
            # Create curve
            curve = axes.plot(
                lambda x: get_y(x, A),
                x_range=[1, 2_000_000],
                color=color,
            )
            
            # Add label
            label = Text(f"A = {A}", font_size=20).next_to(axes, UP)
            
            axes_group.add(axes)
            curves_group.add(curve)
            labels_group.add(label)

        # Show the axes and curves
        self.play(Create(axes_group))
        self.play(Create(curves_group))
        self.play(Write(labels_group))

        # Add explanation text for each curve
        curve_explanations = VGroup(
            Text("Almost constant\nproduct", font_size=20).next_to(axes_group[0], DOWN),
            Text("Balanced\nstableswap", font_size=20).next_to(axes_group[1], DOWN),
            Text("Almost constant\nsum", font_size=20).next_to(axes_group[2], DOWN)
        )
        self.play(Write(curve_explanations))

        # Show trade example on middle curve (A=100)
        current_dot = Dot(axes_group[1].c2p(1_000_000, 1_000_000), color=GREEN)
        trade_size = 100_000
        new_x = 1_000_000 - trade_size
        new_y = get_y(new_x, 100)

        trade_arrow = Arrow(
            start=axes_group[1].c2p(1_000_000, 1_000_000),
            end=axes_group[1].c2p(new_x, new_y),
            color=YELLOW
        )

        trade_info = VGroup(
            Text("Trade Example:", font_size=24),
            Text("Sell 100,000 USDC", font_size=24),
            Text("Low slippage near $1", font_size=24, color=GREEN),
            Text("Higher slippage if pegs break", font_size=24, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT)
        trade_info.next_to(initial_state, DOWN, buff=1)

        self.play(Create(current_dot))
        self.play(Write(trade_info))
        self.play(Create(trade_arrow))

        # Fade out everything except title for key points
        everything_else = VGroup(
            axes_group, curves_group, labels_group, current_dot, trade_arrow,
            initial_state, trade_info, curve_explanations
        )
        self.play(FadeOut(everything_else))

        # Add centered key points
        notes = VGroup(
            Text("Key Points of StableSwap:", font_size=32, color=BLUE),
            Text("• Optimized for tokens of similar value (e.g., stablecoins)", font_size=28),
            Text("• Low slippage when prices are close to peg", font_size=28),
            Text("• Higher slippage when prices deviate significantly", font_size=28),
            Text("• Amplification factor (A) controls curve behavior", font_size=28),
            Text("• More capital efficient than constant product", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(3)

        # Add bonus explanation about amplification coefficient
        self.play(FadeOut(notes))
        
        A_notes = VGroup(
            Text("Understanding the Amplification Coefficient (A):", font_size=32, color=BLUE),
            Text("• A = 1: Behaves like constant product (safer)", font_size=28),
            Text("• A = 100: Normal stablecoin operation", font_size=28),
            Text("• A = 1000: Close to constant sum (efficient)", font_size=28),
            Text("• Higher A = Better rates but more risk", font_size=28),
            Text("• A can be adjusted based on market conditions", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        A_notes.move_to(ORIGIN)

        self.play(Write(A_notes))
        self.wait(3)