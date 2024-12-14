from manim import *
import numpy as np

class CarbonLMMExplainer(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.0f}".format(num)

        # Create title and introduction
        title = Text("Carbon's Logarithmic Market Making (LMM)", font_size=36)
        subtitle = Text("Optimizing for Asset Characteristics", font_size=32, color=BLUE)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)

        # Initial explanation of the concept
        concept = VGroup(
            Text("Traditional AMMs:", font_size=24),
            Text("Use same curve shape for all assets", font_size=24),
            Text("Carbon's Innovation:", font_size=24),
            Text("Adapts curve shape to asset behavior", font_size=24),
            Text("Uses logarithmic pricing for better efficiency", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        concept.to_edge(LEFT).shift(UP)

        self.play(Write(concept))
        self.wait(1)

        # Create coordinate system for price curves
        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 100, 20],
            x_length=6,
            y_length=6,
            tips=False,
            axis_config={"include_numbers": False}
        ).shift(DOWN * 0.5 + RIGHT * 2)

        x_label = Text("Token Amount", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Price", font_size=24).next_to(axes.y_axis, UP)
        
        # Add axis labels
        x_values = VGroup()
        for x in [0, 25, 50, 75, 100]:
            label = Text(str(x), font_size=16)
            label.next_to(axes.c2p(x, 0), DOWN)
            x_values.add(label)

        y_values = VGroup()
        for y in [0, 25, 50, 75, 100]:
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

        # Create different curve types
        def log_curve(x, volatility):
            return 50 + 20 * np.log(x/50) * volatility

        def create_curve(volatility, color, label_text):
            curve = axes.plot(
                lambda x: log_curve(x + 1, volatility),  # Add 1 to avoid log(0)
                x_range=[0, 100],
                color=color
            )
            label = Text(label_text, font_size=20, color=color)
            label.next_to(curve.points[-1], RIGHT)
            return VGroup(curve, label)

        # Create curves for different asset types
        stable_curve = create_curve(0.5, BLUE, "Stablecoin Pair")
        medium_curve = create_curve(1.0, GREEN, "Regular Token")
        volatile_curve = create_curve(2.0, RED, "Volatile Token")

        # Show curves one by one with explanations
        for curve_group, description in [
            (stable_curve, "Stablecoin pairs get flatter curves"),
            (medium_curve, "Regular tokens get balanced curves"),
            (volatile_curve, "Volatile tokens get steeper curves")
        ]:
            self.play(Create(curve_group))
            
            explanation = VGroup(
                Text(description, font_size=24, color=curve_group[0].color),
                Text("Optimizes:", font_size=24),
                Text("• Trading efficiency", font_size=24),
                Text("• Price impact", font_size=24),
                Text("• Capital usage", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT)
            explanation.next_to(concept, DOWN, buff=1)
            
            self.play(Write(explanation))
            self.wait(1)
            if curve_group != volatile_curve:  # Keep last explanation
                self.play(FadeOut(explanation))

        # Fade out everything for key points
        everything_else = VGroup(
            axes, x_label, y_label, x_values, y_values,
            stable_curve, medium_curve, volatile_curve,
            concept, explanation
        )
        self.play(FadeOut(everything_else))

        # Show key points about Carbon LMM
        notes = VGroup(
            Text("Key Innovations of Carbon LMM:", font_size=32, color=BLUE),
            Text("• Logarithmic pricing for natural price movement", font_size=28),
            Text("• Curves adapt to asset characteristics", font_size=28),
            Text("• Optimized capital efficiency per asset type", font_size=28),
            Text("• Better handling of different volatilities", font_size=28),
            Text("• Reduced impermanent loss vs traditional AMMs", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(2)

        # Add mathematical explanation
        self.play(FadeOut(notes))
        
        math_explanation = VGroup(
            Text("How Logarithmic Market Making Works:", font_size=32, color=BLUE),
            Text("1. Analyzes asset volatility patterns", font_size=28),
            Text("2. Adjusts curve steepness accordingly", font_size=28),
            Text("3. Uses logarithmic functions for natural scaling", font_size=28),
            Text("4. Optimizes liquidity distribution", font_size=28),
            Text("5. Continuously adapts to market conditions", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        math_explanation.move_to(ORIGIN)

        self.play(Write(math_explanation))
        self.wait(3)

        # Add benefits section
        self.play(FadeOut(math_explanation))
        
        benefits = VGroup(
            Text("Benefits for Different Assets:", font_size=32, color=BLUE),
            Text("Stablecoins:", font_size=28),
            Text("• Minimal price impact for large trades", font_size=24),
            Text("• High capital efficiency", font_size=24),
            Text("Volatile Tokens:", font_size=28),
            Text("• Better price discovery", font_size=24),
            Text("• Protection against manipulation", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        benefits.move_to(ORIGIN)

        self.play(Write(benefits))
        self.wait(3)