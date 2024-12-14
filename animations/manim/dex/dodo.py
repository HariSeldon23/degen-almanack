from manim import *
import numpy as np

class DODOPMMExplainer(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.0f}".format(num)

        # Create title and introduction
        title = Text("DODO's Proactive Market Maker (PMM)", font_size=36)
        subtitle = Text("Oracle-Guided Dynamic Pricing", font_size=32, color=BLUE)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)

        # Initial concept explanation
        concept = VGroup(
            Text("Traditional AMMs:", font_size=24),
            Text("• Rely on arbitrage for price discovery", font_size=24),
            Text("• Static mathematical formulas", font_size=24),
            Text("DODO PMM Innovation:", font_size=24),
            Text("• Uses price oracles for guidance", font_size=24),
            Text("• Dynamically adjusts liquidity curves", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        concept.to_edge(LEFT).shift(UP)

        self.play(Write(concept))
        self.wait(1)

        # Create coordinate system for price curves
        axes = Axes(
            x_range=[0, 200, 50],
            y_range=[2000, 4000, 500],
            x_length=8,
            y_length=4,
            tips=False,
            axis_config={"include_numbers": False}
        ).shift(DOWN * 0.5)

        x_label = Text("ETH Amount", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Price (USDC)", font_size=24).next_to(axes.y_axis, UP)
        
        # Add axis labels
        x_values = VGroup()
        for x in [0, 50, 100, 150, 200]:
            label = Text(str(x), font_size=16)
            label.next_to(axes.c2p(x, 2000), DOWN)
            x_values.add(label)

        y_values = VGroup()
        for y in [2000, 2500, 3000, 3500, 4000]:
            label = Text(f"${y}", font_size=16)
            label.next_to(axes.c2p(0, y), LEFT)
            y_values.add(label)

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(x_values),
            Write(y_values)
        )

        # Create oracle price line
        oracle_price = 3000
        oracle_line = DashedLine(
            axes.c2p(0, oracle_price),
            axes.c2p(200, oracle_price),
            color=YELLOW
        )
        oracle_label = Text("Oracle Price", font_size=20, color=YELLOW)
        oracle_label.next_to(oracle_line, RIGHT)

        self.play(
            Create(oracle_line),
            Write(oracle_label)
        )

        # Create PMM curve function
        def pmm_price(x, base_price=3000, amplitude=500, k=0.1):
            return base_price + amplitude * (1 - np.exp(-k * abs(x - 100)))

        # Create PMM curves for different market states
        curves = []
        labels = []
        states = [
            ("Balanced Market", BLUE, 0),
            ("High Demand", GREEN, 200),
            ("Low Demand", RED, -200)
        ]

        for state, color, offset in states:
            curve = axes.plot(
                lambda x: pmm_price(x, oracle_price + offset),
                x_range=[0, 200],
                color=color
            )
            curves.append(curve)
            
            label = Text(state, font_size=20, color=color)
            label.next_to(curve, RIGHT)
            labels.append(label)

        # Show curves one by one with explanations
        for i, (curve, label, (state, color, _)) in enumerate(zip(curves, labels, states)):
            self.play(Create(curve), Write(label))
            
            explanation = VGroup(
                Text(f"{state}:", font_size=24, color=color),
                Text("PMM adjusts curve based on:", font_size=24),
                Text("• Oracle price feed", font_size=24),
                Text("• Market demand", font_size=24),
                Text("• Available liquidity", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT)
            explanation.next_to(concept, DOWN, buff=1)
            
            self.play(Write(explanation))
            self.wait(1)
            if i < len(curves) - 1:
                self.play(FadeOut(explanation))

        # Fade out everything for key points
        everything_else = VGroup(
            axes, x_label, y_label, x_values, y_values, oracle_line, oracle_label,
            *curves, *labels, concept, explanation
        )
        self.play(FadeOut(everything_else))

        # Show key points about PMM
        notes = VGroup(
            Text("Key Innovations of DODO PMM:", font_size=32, color=BLUE),
            Text("• Oracles provide external price reference", font_size=28),
            Text("• Curves adjust based on market conditions", font_size=28),
            Text("• Reduced impermanent loss for LPs", font_size=28),
            Text("• More efficient capital utilization", font_size=28),
            Text("• Better prices for traders near oracle price", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(2)

        # Add explanation of how PMM works
        self.play(FadeOut(notes))
        
        mechanism = VGroup(
            Text("How PMM Works:", font_size=32, color=BLUE),
            Text("1. Oracle provides market price", font_size=28),
            Text("2. Algorithm measures supply/demand", font_size=28),
            Text("3. Price curve shifts dynamically", font_size=28),
            Text("4. Liquidity concentrates near market price", font_size=28),
            Text("5. Arbitrage opportunities minimized", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        mechanism.move_to(ORIGIN)

        self.play(Write(mechanism))
        self.wait(3)

        # Add benefits section
        self.play(FadeOut(mechanism))
        
        benefits = VGroup(
            Text("Key Benefits:", font_size=32, color=BLUE),
            Text("For Traders:", font_size=28),
            Text("• Better prices near market rate", font_size=24),
            Text("• Lower slippage on large trades", font_size=24),
            Text("For Liquidity Providers:", font_size=28),
            Text("• Reduced impermanent loss risk", font_size=24),
            Text("• More efficient capital usage", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        benefits.move_to(ORIGIN)

        self.play(Write(benefits))
        self.wait(3)