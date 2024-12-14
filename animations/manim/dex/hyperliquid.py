from manim import *
import numpy as np

class HyperliquidExplainer(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.0f}".format(num)

        # Create title and introduction
        title = Text("Hyperliquid: Pro-rata Market Making", font_size=36)
        subtitle = Text("Multi-Collateral Perpetual Futures", font_size=32, color=BLUE)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)

        # Initial concept explanation
        concept = VGroup(
            Text("Traditional Perps:", font_size=24),
            Text("Order book or AMM based", font_size=24),
            Text("Hyperliquid Innovation:", font_size=24),
            Text("Pro-rata market making", font_size=24),
            Text("Multi-collateral system", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        concept.to_edge(LEFT).shift(UP)

        self.play(Write(concept))
        self.wait(1)

        # Create liquidity pool visualization
        pool = Circle(radius=1.5, color=BLUE)
        pool.shift(DOWN * 0.5)
        pool_label = Text("Liquidity Pool", font_size=24)
        pool_label.next_to(pool, UP)

        # Create collateral types
        collaterals = VGroup()
        collateral_labels = VGroup()
        
        colors = [RED, GREEN, YELLOW]
        types = ["USDC", "ETH", "BTC"]
        
        for i, (color, type) in enumerate(zip(colors, types)):
            circle = Circle(radius=0.3, color=color, fill_opacity=0.4)
            circle.shift(pool.get_center() + UP * 0.5 + RIGHT * (i - 1))
            label = Text(type, font_size=20, color=color)
            label.next_to(circle, UP)
            collaterals.add(circle)
            collateral_labels.add(label)

        self.play(
            Create(pool),
            Write(pool_label)
        )
        self.play(
            AnimationGroup(
                *[Create(c) for c in collaterals],
                *[Write(l) for l in collateral_labels],
                lag_ratio=0.2
            )
        )

        # Show market maker positions
        mm_positions = VGroup()
        mm_labels = VGroup()
        
        for i in range(4):
            angle = i * PI/2
            pos = Dot(
                pool.point_at_angle(angle),
                color=WHITE
            )
            label = Text(f"MM {i+1}", font_size=16)
            label.next_to(pos, pos.get_center() - pool.get_center())
            mm_positions.add(pos)
            mm_labels.add(label)

        self.play(
            AnimationGroup(
                *[Create(p) for p in mm_positions],
                *[Write(l) for l in mm_labels],
                lag_ratio=0.2
            )
        )

        # Show trade flow
        trade_start = Dot(color=WHITE)
        trade_start.move_to(UP * 2 + LEFT * 3)
        trade_label = Text("Long 10 ETH", font_size=20)
        trade_label.next_to(trade_start, UP)

        # Create multiple arrows to show pro-rata distribution
        arrows = VGroup()
        for pos in mm_positions:
            arrow = Arrow(
                trade_start.get_center(),
                pos.get_center(),
                color=YELLOW,
                buff=0.2
            )
            arrows.add(arrow)

        self.play(
            Create(trade_start),
            Write(trade_label)
        )
        self.play(
            AnimationGroup(
                *[Create(arrow) for arrow in arrows],
                lag_ratio=0.2
            )
        )

        # Show pro-rata distribution
        distributions = VGroup()
        for i, pos in enumerate(mm_positions):
            amount = Text(f"2.5 ETH", font_size=16, color=YELLOW)
            amount.next_to(arrows[i].get_center(), RIGHT)
            distributions.add(amount)

        self.play(Write(distributions))

        # Show matching engine explanation
        matching = VGroup(
            Text("Pro-rata Matching:", font_size=24, color=BLUE),
            Text("• Trade split among MMs", font_size=20),
            Text("• Based on capital ratio", font_size=20),
            Text("• Instant settlement", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT)
        matching.to_edge(RIGHT)

        self.play(Write(matching))
        self.wait(1)

        # Fade out everything for key points
        everything_else = VGroup(
            pool, pool_label, collaterals, collateral_labels,
            mm_positions, mm_labels, trade_start, trade_label,
            arrows, distributions, matching, concept
        )
        self.play(FadeOut(everything_else))

        # Show key points about Hyperliquid
        notes = VGroup(
            Text("Key Innovations:", font_size=32, color=BLUE),
            Text("• Pro-rata order matching", font_size=28),
            Text("• Multiple collateral types", font_size=28),
            Text("• Instant settlement", font_size=28),
            Text("• Shared liquidity pool", font_size=28),
            Text("• Reduced market impact", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(2)

        # Show technical details
        self.play(FadeOut(notes))
        
        technical = VGroup(
            Text("How It Works:", font_size=32, color=BLUE),
            Text("1. Traders submit orders", font_size=28),
            Text("2. System calculates pro-rata shares", font_size=28),
            Text("3. Matches across all MMs", font_size=28),
            Text("4. Settles instantly on-chain", font_size=28),
            Text("5. Updates positions atomically", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        technical.move_to(ORIGIN)

        self.play(Write(technical))
        self.wait(3)

        # Add advantages section
        self.play(FadeOut(technical))
        
        advantages = VGroup(
            Text("System Advantages:", font_size=32, color=BLUE),
            Text("For Traders:", font_size=28),
            Text("• Better price execution", font_size=24),
            Text("• Lower slippage", font_size=24),
            Text("For Market Makers:", font_size=28),
            Text("• Simplified position management", font_size=24),
            Text("• Efficient capital utilization", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        advantages.move_to(ORIGIN)

        self.play(Write(advantages))
        self.wait(3)