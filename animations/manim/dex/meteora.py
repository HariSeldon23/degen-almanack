from manim import *
import numpy as np

class MeteoraExplainer(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.0f}".format(num)

        # Create title and introduction
        title = Text("Meteora's Dynamic Position AMM (DyP)", font_size=36)
        subtitle = Text("Automated Liquidity Management", font_size=32, color=BLUE)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)

        # Initial comparison explanation
        concept = VGroup(
            Text("Traditional Concentrated Liquidity:", font_size=24),
            Text("Manual position management", font_size=24),
            Text("Meteora Innovation:", font_size=24),
            Text("Automatic position adjustment", font_size=24),
            Text("Dynamic price range tracking", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        concept.to_edge(LEFT).shift(UP)

        self.play(Write(concept))
        self.wait(1)

        # Create price chart axes
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[2000, 4000, 500],
            x_length=8,
            y_length=4,
            tips=False,
            axis_config={"include_numbers": False}
        ).shift(DOWN * 0.5)

        x_label = Text("Time", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("ETH Price (USDC)", font_size=24).next_to(axes.y_axis, UP)
        
        # Add price labels
        y_values = VGroup()
        for y in range(2000, 4001, 500):
            label = Text(f"${y}", font_size=16)
            label.next_to(axes.c2p(0, y), LEFT)
            y_values.add(label)

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(y_values)
        )

        # Create price movement curve
        def price_function(x):
            return 3000 + 500 * np.sin(x) + 200 * np.sin(2*x)

        price_curve = axes.plot(
            price_function,
            x_range=[0, 10],
            color=WHITE
        )

        self.play(Create(price_curve))

        # Create moving price point
        moving_dot = Dot(color=YELLOW)
        moving_dot.move_to(axes.c2p(0, price_function(0)))

        # Create traditional liquidity range (static)
        traditional_range = Rectangle(
            height=1,
            width=8,
            stroke_color=RED,
            fill_color=RED,
            fill_opacity=0.2
        )
        traditional_range.move_to(axes.c2p(5, 3000))
        trad_label = Text("Traditional Static Range", font_size=20, color=RED)
        trad_label.next_to(traditional_range, UP)

        self.play(
            Create(traditional_range),
            Write(trad_label)
        )

        # Create dynamic range that follows price
        dynamic_range = Rectangle(
            height=0.5,
            width=1,
            stroke_color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.3
        )
        dynamic_label = Text("Dynamic Position", font_size=20, color=GREEN)
        dynamic_label.next_to(dynamic_range, UP)

        self.play(
            Create(dynamic_range),
            Write(dynamic_label)
        )

        # Animate price movement and dynamic range adjustment
        def update_position(mob, alpha):
            x = alpha * 10
            new_y = price_function(x)
            moving_dot.move_to(axes.c2p(x, new_y))
            
            # Update dynamic range position
            range_height = axes.y_length * 500 / 2000  # 500 USDC range
            dynamic_range.height = range_height
            dynamic_range.move_to(axes.c2p(x, new_y))
            
            # Update label position
            dynamic_label.next_to(dynamic_range, UP)

        self.play(
            UpdateFromAlphaFunc(dynamic_range, update_position),
            MoveAlong(moving_dot, price_curve),
            rate_func=linear,
            run_time=5
        )
        self.wait(1)

        # Show efficiency comparison
        comparison = VGroup(
            Text("Efficiency Comparison:", font_size=24, color=BLUE),
            Text("Traditional: Wide static range", font_size=20, color=RED),
            Text("DyP: Focused dynamic range", font_size=20, color=GREEN),
            Text("→ Better capital efficiency", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT)
        comparison.to_edge(RIGHT)

        self.play(Write(comparison))
        self.wait(1)

        # Fade out everything for key points
        everything_else = VGroup(
            axes, x_label, y_label, y_values, price_curve,
            moving_dot, traditional_range, trad_label,
            dynamic_range, dynamic_label, comparison, concept
        )
        self.play(FadeOut(everything_else))

        # Show key points about DyP
        notes = VGroup(
            Text("Key Innovations of DyP:", font_size=32, color=BLUE),
            Text("• Automatic position adjustment", font_size=28),
            Text("• No manual rebalancing needed", font_size=28),
            Text("• Higher capital efficiency", font_size=28),
            Text("• Lower maintenance costs", font_size=28),
            Text("• Reduced impermanent loss risk", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(2)

        # Show mechanism details
        self.play(FadeOut(notes))
        
        mechanism = VGroup(
            Text("How DyP Works:", font_size=32, color=BLUE),
            Text("1. Monitors price movements", font_size=28),
            Text("2. Adjusts position boundaries", font_size=28),
            Text("3. Optimizes liquidity depth", font_size=28),
            Text("4. Rebalances automatically", font_size=28),
            Text("5. Maintains optimal ranges", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        mechanism.move_to(ORIGIN)

        self.play(Write(mechanism))
        self.wait(3)

        # Add benefits section
        self.play(FadeOut(mechanism))
        
        benefits = VGroup(
            Text("Benefits for Users:", font_size=32, color=BLUE),
            Text("For LPs:", font_size=28),
            Text("• Set-and-forget positions", font_size=24),
            Text("• Better yield generation", font_size=24),
            Text("For Traders:", font_size=28),
            Text("• More consistent liquidity", font_size=24),
            Text("• Lower slippage", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        benefits.move_to(ORIGIN)

        self.play(Write(benefits))
        self.wait(3)