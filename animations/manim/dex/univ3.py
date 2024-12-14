from manim import *
import numpy as np

class UniswapV3Explainer(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.0f}".format(num)

        # Create title and introduction
        title = Text("Uniswap V3: Concentrated Liquidity", font_size=36)
        subtitle = Text("x * y = k within price ranges", font_size=32, color=BLUE)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)

        # Initial explanation of the concept
        concept = VGroup(
            Text("Traditional AMM (V2):", font_size=24),
            Text("Liquidity spread across all prices", font_size=24),
            Text("→", font_size=24),
            Text("Concentrated Liquidity (V3):", font_size=24),
            Text("Liquidity focused in specific ranges", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        concept.to_edge(LEFT).shift(UP)

        self.play(Write(concept))
        self.wait(1)

        # Create coordinate system for price ranges
        axes = Axes(
            x_range=[0, 5000, 1000],
            y_range=[0, 1, 0.2],
            x_length=8,
            y_length=4,
            tips=False,
            axis_config={"include_numbers": False}
        ).shift(DOWN * 0.5)

        x_label = Text("ETH Price in USDC", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Liquidity", font_size=24).next_to(axes.y_axis, UP)
        
        # Add price labels
        x_values = VGroup()
        for x in [0, 1000, 2000, 3000, 4000, 5000]:
            label = Text(f"${x}", font_size=16)
            label.next_to(axes.c2p(x, 0), DOWN)
            x_values.add(label)

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(x_values)
        )

        # Create different liquidity positions
        def create_position(start_price, end_price, height, color):
            points = [
                axes.c2p(start_price, 0),
                axes.c2p(start_price, height),
                axes.c2p(end_price, height),
                axes.c2p(end_price, 0)
            ]
            position = Polygon(*points, fill_opacity=0.4, fill_color=color, color=color)
            label = Text(f"${start_price}-${end_price}", font_size=16, color=color)
            label.next_to(position, UP)
            return VGroup(position, label)

        # Create multiple liquidity positions
        position1 = create_position(2800, 3200, 0.3, BLUE)  # Narrow range around 3000
        position2 = create_position(2500, 3500, 0.2, GREEN)  # Medium range
        position3 = create_position(2000, 4000, 0.1, RED)    # Wide range

        # Show positions one by one
        for i, position in enumerate([position1, position2, position3]):
            self.play(Create(position))
            
            # Add explanation for each position
            explanation = VGroup(
                Text(f"Position {i+1}:", font_size=24),
                Text(f"Price Range: {position[1].text}", font_size=24),
                Text("Higher concentration = Better rates", font_size=24 if i == 0 else 20)
            ).arrange(DOWN, aligned_edge=LEFT)
            explanation.next_to(concept, DOWN, buff=1)
            self.play(Write(explanation))
            self.wait(1)
            if i < 2:  # Don't remove the last explanation
                self.play(FadeOut(explanation))

        # Show combined liquidity effect
        combined_effect = VGroup(
            Text("Combined Effect:", font_size=24, color=BLUE),
            Text("• More liquidity = Lower slippage", font_size=24),
            Text("• Stacked ranges = Better rates", font_size=24),
            Text("• Capital efficiency ↑", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        combined_effect.to_edge(RIGHT)

        self.play(Write(combined_effect))
        self.wait(1)

        # Fade out positions and explanations for key points
        everything_else = VGroup(
            axes, x_label, y_label, x_values, position1, position2, position3,
            concept, explanation, combined_effect
        )
        self.play(FadeOut(everything_else))

        # Show key points about V3
        notes = VGroup(
            Text("Key Innovations of Uniswap V3:", font_size=32, color=BLUE),
            Text("• Liquidity providers choose specific price ranges", font_size=28),
            Text("• Capital efficiency can be 4000x better than V2", font_size=28),
            Text("• Multiple positions can be created by same LP", font_size=28),
            Text("• Enables active liquidity management", font_size=28),
            Text("• Higher returns but more complex to manage", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(2)

        # Add practical implications
        self.play(FadeOut(notes))
        
        implications = VGroup(
            Text("Practical Implications:", font_size=32, color=BLUE),
            Text("• Better rates for traders in active ranges", font_size=28),
            Text("• LPs can concentrate around current price", font_size=28),
            Text("• Impermanent loss risk still exists", font_size=28),
            Text("• Requires more active management", font_size=28),
            Text("• Ideal for range-bound trading", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        implications.move_to(ORIGIN)

        self.play(Write(implications))
        self.wait(3)