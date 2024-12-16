from manim import *
import numpy as np

class SlipstreamExplainer(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.0f}".format(num)

        # Create title and introduction
        title = Text("Velodrome's Slipstream: Multi-Route Pooling", font_size=36)
        subtitle = Text("Solving Pool Overcrowding", font_size=32, color=BLUE)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)

        # Initial problem explanation
        problem = VGroup(
            Text("Traditional AMM Problem:", font_size=24),
            Text("Single large pool = High slippage", font_size=24),
            Text("Slipstream Solution:", font_size=24),
            Text("Multiple coordinated pools", font_size=24),
            Text("Automatic liquidity balancing", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        problem.to_edge(LEFT).shift(UP)

        self.play(Write(problem))
        self.wait(1)

        # Create visualization of traditional vs Slipstream approach
        # First, create traditional single pool visualization
        traditional_pool = Circle(radius=1, color=BLUE)
        traditional_pool.shift(LEFT * 3 + DOWN)
        traditional_label = Text("Traditional\nSingle Pool", font_size=20)
        traditional_label.next_to(traditional_pool, UP)
        
        # Add liquidity indicators to traditional pool
        traditional_liquidity = Text("$10M", font_size=20, color=BLUE)
        traditional_liquidity.move_to(traditional_pool)

        self.play(
            Create(traditional_pool),
            Write(traditional_label),
            Write(traditional_liquidity)
        )

        # Create Slipstream multiple pools
        slipstream_pools = VGroup()
        pool_labels = VGroup()
        pool_amounts = ["$4M", "$3M", "$3M"]
        
        for i in range(3):
            pool = Circle(radius=0.6, color=GREEN)
            pool.shift(RIGHT * (2 + i * 2) + DOWN)
            amount = Text(pool_amounts[i], font_size=20, color=GREEN)
            amount.move_to(pool)
            slipstream_pools.add(pool)
            pool_labels.add(amount)

        slipstream_label = Text("Slipstream Multiple Pools", font_size=20)
        slipstream_label.next_to(slipstream_pools, UP)

        self.play(
            Create(slipstream_pools),
            Write(slipstream_label),
            Write(pool_labels)
        )

        # Add connecting arrows between Slipstream pools
        arrows = VGroup()
        for i in range(2):
            arrow1 = Arrow(
                slipstream_pools[i].get_right(),
                slipstream_pools[i+1].get_left(),
                color=YELLOW
            )
            arrow2 = Arrow(
                slipstream_pools[i+1].get_left(),
                slipstream_pools[i].get_right(),
                color=YELLOW
            ).shift(UP * 0.2)
            arrows.add(arrow1, arrow2)

        self.play(Create(arrows))

        # Show trade example
        trade_info = VGroup(
            Text("Trade Example: Sell 1M USDC", font_size=24, color=RED),
            Text("Traditional: All impact in one pool", font_size=24),
            Text("Slipstream: Split across pools", font_size=24, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT)
        trade_info.to_edge(RIGHT).shift(UP)

        self.play(Write(trade_info))
        
        # Animate trade impact
        impact_traditional = Text("-3% price impact", font_size=20, color=RED)
        impact_traditional.next_to(traditional_pool, DOWN)
        
        impact_slipstream = Text("-1% price impact", font_size=20, color=GREEN)
        impact_slipstream.next_to(slipstream_pools[1], DOWN)

        self.play(Write(impact_traditional), Write(impact_slipstream))
        self.wait(1)

        # Fade out everything for key points
        everything_else = VGroup(
            traditional_pool, traditional_label, traditional_liquidity,
            slipstream_pools, slipstream_label, pool_labels, arrows,
            problem, trade_info, impact_traditional, impact_slipstream
        )
        self.play(FadeOut(everything_else))

        # Show key points about Slipstream
        notes = VGroup(
            Text("Key Innovations of Slipstream:", font_size=32, color=BLUE),
            Text("• Multiple coordinated liquidity pools", font_size=28),
            Text("• Automatic trade route optimization", font_size=28),
            Text("• Reduced price impact for large trades", font_size=28),
            Text("• Better capital efficiency", font_size=28),
            Text("• Lower slippage across all trade sizes", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(2)

        # Show technical details
        self.play(FadeOut(notes))
        
        technical = VGroup(
            Text("How Slipstream Works:", font_size=32, color=BLUE),
            Text("1. Creates multiple pools for same pair", font_size=28),
            Text("2. Balances liquidity across pools", font_size=28),
            Text("3. Routes trades optimally", font_size=28),
            Text("4. Adjusts to trading volume", font_size=28),
            Text("5. Maintains price consistency", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        technical.move_to(ORIGIN)

        self.play(Write(technical))
        self.wait(3)

        # Add benefits section
        self.play(FadeOut(technical))
        
        benefits = VGroup(
            Text("Benefits for Different Users:", font_size=32, color=BLUE),
            Text("For Traders:", font_size=28),
            Text("• Better prices on large trades", font_size=24),
            Text("• Reduced slippage", font_size=24),
            Text("For Liquidity Providers:", font_size=28),
            Text("• More efficient capital usage", font_size=24),
            Text("• Better fee generation", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        benefits.move_to(ORIGIN)

        self.play(Write(benefits))
        self.wait(3)