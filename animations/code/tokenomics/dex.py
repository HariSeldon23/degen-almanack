from manim import *
import numpy as np

class TokenEconomics(Scene):
    def construct(self):
        # Create the axes with more room for labels
        axes = Axes(
            x_range=[0, 48, 12],  # 48 months (4 years)
            y_range=[0, 2, 0.25],  # Price range from 0 to 2 dollars
            x_length=10,
            y_length=6,
            axis_config={
                "color": BLUE,
                "include_numbers": True,
                "numbers_to_include": [0, 12, 24, 36, 48],  # Show yearly marks
            },
            tips=False
        ).to_edge(DOWN, buff=1.5)  # Move axes down to make room for titles
        
        # Add properly positioned labels with more space
        x_label = Text("Months", font_size=24).next_to(axes.x_axis, DOWN, buff=0.5)
        y_label = Text("Price ($)", font_size=24).next_to(axes.y_axis, LEFT, buff=0.5).rotate(90 * DEGREES)
        
        # Initial market price at $1
        initial_price = 1
        
        # Define emission schedule (percentage of total supply released each year)
        # Year 1: 40%, Year 2: 30%, Year 3: 20%, Year 4: 10%
        def get_supply_multiplier(month):
            year = month // 12
            if year == 0:
                return 1 + (month * 0.4 / 12)  # Year 1: 40% increase
            elif year == 1:
                return 1.4 + ((month - 12) * 0.3 / 12)  # Year 2: 30% increase
            elif year == 2:
                return 1.7 + ((month - 24) * 0.2 / 12)  # Year 3: 20% increase
            else:
                return 1.9 + ((month - 36) * 0.1 / 12)  # Year 4: 10% increase

        # Create price curve based on emissions
        def price_curve(x):
            return initial_price / get_supply_multiplier(x)
        
        price_line = axes.plot(price_curve, color=YELLOW)
        
        # Create emission schedule labels
        emission_labels = VGroup()
        years = ["Year 1: 40%", "Year 2: 30%", "Year 3: 20%", "Year 4: 10%"]
        for i, label in enumerate(years):
            text = Text(label, font_size=20, color=WHITE)
            text.move_to(axes.coords_to_point(i * 12 + 6, 1.8))
            emission_labels.add(text)
        
        # Initial setup
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label)
        )
        
        # Show initial price
        initial_title = Text("Initial Token Price: $1.00", font_size=36).to_edge(UP, buff=1)
        self.play(Write(initial_title))
        self.wait(1)
        
        # Show emission schedule
        emission_title = Text("4-Year Token Emission Schedule", font_size=36).next_to(initial_title, DOWN)
        self.play(Write(emission_title))
        self.play(AnimationGroup(*[Write(label) for label in emission_labels]))
        self.wait(1)
        
        # Animate price curve
        self.play(
            Create(price_line),
            run_time=3
        )
        
        # Add key price points
        points = []
        labels = []
        for month in [0, 12, 24, 36, 48]:
            price = price_curve(month)
            point = Dot(axes.coords_to_point(month, price), color=RED)
            label = Text(f"${price:.2f}", font_size=20, color=RED)
            label.next_to(point, UP, buff=0.2)
            points.append(point)
            labels.append(label)
        
        self.play(
            *[Create(point) for point in points],
            *[Write(label) for label in labels]
        )
        
        # Add explanation
        explanation = Text(
            "Without sustained demand growth, token emissions lead to price decline\n"
            "as more tokens enter circulation each year",
            font_size=24,
            line_spacing=1.5
        ).to_edge(DOWN, buff=0.2)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # Add note about speculation
        speculation_note = Text(
            "Note: Actual prices may temporarily rise due to speculation,\n"
            "but natural selling pressure remains from emissions",
            font_size=20,
            color=YELLOW
        ).next_to(explanation, UP, buff=0.5)
        
        self.play(Write(speculation_note))
        self.wait(3)