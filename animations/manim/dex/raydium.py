from manim import *
import numpy as np

class RaydiumExplainer(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.0f}".format(num)

        # Create title and introduction
        title = Text("Raydium's Hybrid Liquidity Model", font_size=36)
        subtitle = Text("AMM + Order Book Integration", font_size=32, color=BLUE)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)

        # Initial explanation
        concept = VGroup(
            Text("Traditional AMMs:", font_size=24),
            Text("Single liquidity source", font_size=24),
            Text("Raydium Innovation:", font_size=24),
            Text("Combines AMM pools + Serum order book", font_size=24),
            Text("Smart routing for best execution", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        concept.to_edge(LEFT).shift(UP)

        self.play(Write(concept))
        self.wait(1)

        # Create visualization of both liquidity sources
        # First, create AMM pool
        amm_pool = Circle(radius=1, color=BLUE)
        amm_pool.shift(LEFT * 3 + DOWN)
        amm_label = Text("AMM Pool\n$1M", font_size=20)
        amm_label.next_to(amm_pool, UP)

        # Create order book visualization
        orderbook = Rectangle(height=2, width=1.5, color=GREEN)
        orderbook.shift(RIGHT * 3 + DOWN)
        ob_label = Text("Serum Order Book\n$2M", font_size=20)
        ob_label.next_to(orderbook, UP)

        # Add buy/sell orders to order book
        orders = VGroup()
        for i in range(5):
            # Buy orders (green)
            buy = Line(
                orderbook.get_left() + RIGHT * 0.1 + UP * (0.8 - i * 0.3),
                orderbook.get_right() + LEFT * 0.1 + UP * (0.8 - i * 0.3),
                color=GREEN
            )
            # Sell orders (red)
            sell = Line(
                orderbook.get_left() + RIGHT * 0.1 + DOWN * (0.8 - i * 0.3),
                orderbook.get_right() + LEFT * 0.1 + DOWN * (0.8 - i * 0.3),
                color=RED
            )
            orders.add(buy, sell)

        self.play(
            Create(amm_pool),
            Write(amm_label),
            Create(orderbook),
            Write(ob_label),
            Create(orders)
        )

        # Create connecting arrows between sources
        arrows = VGroup(
            Arrow(amm_pool.get_right(), orderbook.get_left(), color=YELLOW),
            Arrow(orderbook.get_left(), amm_pool.get_right(), color=YELLOW).shift(UP * 0.2)
        )
        arrow_label = Text("Hybrid\nLiquidity", font_size=20, color=YELLOW)
        arrow_label.next_to(arrows, UP)

        self.play(
            Create(arrows),
            Write(arrow_label)
        )

        # Show trade routing example
        trade_start = Dot(color=WHITE).move_to(UP * 2)
        trade_label = Text("Trade: Sell 100k USDC", font_size=20).next_to(trade_start, RIGHT)

        self.play(Create(trade_start), Write(trade_label))

        # Show trade splitting
        split_arrows = VGroup(
            Arrow(trade_start.get_center(), amm_pool.get_top(), color=BLUE),
            Arrow(trade_start.get_center(), orderbook.get_top(), color=GREEN)
        )
        
        split_labels = VGroup(
            Text("40k", font_size=16, color=BLUE).next_to(split_arrows[0].get_center(), LEFT),
            Text("60k", font_size=16, color=GREEN).next_to(split_arrows[1].get_center(), RIGHT)
        )

        self.play(
            Create(split_arrows),
            Write(split_labels)
        )

        # Show execution results
        results = VGroup(
            Text("AMM Pool: Less Slippage", font_size=20, color=BLUE),
            Text("Order Book: Better Price", font_size=20, color=GREEN),
            Text("Result: Optimal Execution", font_size=20, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT)
        results.to_edge(RIGHT)

        self.play(Write(results))
        self.wait(1)

        # Fade out everything for key points
        everything_else = VGroup(
            amm_pool, amm_label, orderbook, ob_label, orders,
            arrows, arrow_label, trade_start, trade_label,
            split_arrows, split_labels, results, concept
        )
        self.play(FadeOut(everything_else))

        # Show key points about Raydium
        notes = VGroup(
            Text("Key Innovations of Raydium:", font_size=32, color=BLUE),
            Text("• Combines AMM and order book liquidity", font_size=28),
            Text("• Smart routing between liquidity sources", font_size=28),
            Text("• Better pricing through competition", font_size=28),
            Text("• Lower slippage on large trades", font_size=28),
            Text("• Higher capital efficiency", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(2)

        # Show technical details
        self.play(FadeOut(notes))
        
        technical = VGroup(
            Text("How Raydium Works:", font_size=32, color=BLUE),
            Text("1. Checks prices in both sources", font_size=28),
            Text("2. Calculates optimal split", font_size=28),
            Text("3. Routes portions of trade", font_size=28),
            Text("4. Executes simultaneously", font_size=28),
            Text("5. Settles on Solana for speed", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        technical.move_to(ORIGIN)

        self.play(Write(technical))
        self.wait(3)

        # Add benefits section
        self.play(FadeOut(technical))
        
        benefits = VGroup(
            Text("Benefits for Users:", font_size=32, color=BLUE),
            Text("For Traders:", font_size=28),
            Text("• Better prices through competition", font_size=24),
            Text("• Lower slippage on large trades", font_size=24),
            Text("For Liquidity Providers:", font_size=28),
            Text("• Multiple revenue streams", font_size=24),
            Text("• Reduced impermanent loss risk", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        benefits.move_to(ORIGIN)

        self.play(Write(benefits))
        self.wait(3)