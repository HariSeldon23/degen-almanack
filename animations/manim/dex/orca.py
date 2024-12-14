from manim import *
import numpy as np

class OrcaWhirlpoolsExplainer(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.0f}".format(num)

        # Create title and introduction
        title = Text("Orca Whirlpools: Advanced Concentrated Liquidity", font_size=36)
        subtitle = Text("Built for Solana's High Performance", font_size=32, color=BLUE)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)

        # Initial explanation
        concept = VGroup(
            Text("Traditional Concentrated Liquidity:", font_size=24),
            Text("Individual position management", font_size=24),
            Text("Whirlpools Innovation:", font_size=24),
            Text("Standardized tick arrays", font_size=24),
            Text("Optimized for Solana's architecture", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        concept.to_edge(LEFT).shift(UP)

        self.play(Write(concept))
        self.wait(1)

        # Create main price range visualization
        axes = Axes(
            x_range=[1500, 4500, 500],
            y_range=[0, 1.5, 0.5],
            x_length=8,
            y_length=4,
            tips=False,
            axis_config={"include_numbers": False}
        ).shift(DOWN * 0.5)

        x_label = Text("ETH Price (USDC)", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Liquidity Depth", font_size=24).next_to(axes.y_axis, UP)
        
        # Add price labels
        x_values = VGroup()
        for x in range(1500, 4501, 500):
            label = Text(f"${x}", font_size=16)
            label.next_to(axes.c2p(x, 0), DOWN)
            x_values.add(label)

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(x_values)
        )

        # Create tick arrays (whirlpools)
        current_price = 3000
        tick_size = 100  # Size of each tick array
        whirlpools = VGroup()
        pool_labels = VGroup()

        # Create multiple tick arrays around current price
        for i in range(-5, 6):
            start_price = current_price + (i * tick_size)
            height = 0.8 * np.exp(-0.1 * abs(i))  # Higher liquidity near current price
            
            pool = Rectangle(
                height=height,
                width=tick_size,
                fill_color=BLUE if i == 0 else GREEN,
                fill_opacity=0.4,
                stroke_color=BLUE if i == 0 else GREEN
            )
            pool.move_to(axes.c2p(start_price + tick_size/2, height/2))
            
            if i == 0:
                label = Text("Current\nWhirlpool", font_size=16, color=BLUE)
            elif abs(i) == 1:
                label = Text("Adjacent\nWhirlpool", font_size=16, color=GREEN)
            else:
                label = Text(f"±{abs(i)}\nWhirlpool", font_size=16, color=GREEN)
            
            label.next_to(pool, UP)
            
            whirlpools.add(pool)
            pool_labels.add(label)

        self.play(
            AnimationGroup(*[Create(pool) for pool in whirlpools], lag_ratio=0.1)
        )
        self.play(
            AnimationGroup(*[Write(label) for label in pool_labels], lag_ratio=0.1)
        )

        # Show position management
        position_info = VGroup(
            Text("Position Management:", font_size=24, color=BLUE),
            Text("• Positions snap to tick arrays", font_size=20),
            Text("• Automatic rebalancing", font_size=20),
            Text("• Gas-efficient on Solana", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT)
        position_info.to_edge(RIGHT).shift(UP)

        self.play(Write(position_info))
        
        # Show trade example
        trade_start = Dot(color=WHITE).move_to(axes.c2p(2800, 1.2))
        trade_end = Dot(color=RED).move_to(axes.c2p(3200, 1.2))
        trade_arrow = Arrow(trade_start.get_center(), trade_end.get_center(), color=YELLOW)
        
        trade_label = Text("Trade across multiple Whirlpools", font_size=20, color=YELLOW)
        trade_label.next_to(trade_arrow, UP)

        self.play(
            Create(trade_start),
            Create(trade_end),
            Create(trade_arrow),
            Write(trade_label)
        )
        self.wait(1)

        # Fade out everything for key points
        everything_else = VGroup(
            axes, x_label, y_label, x_values, whirlpools, pool_labels,
            position_info, trade_start, trade_end, trade_arrow, trade_label,
            concept
        )
        self.play(FadeOut(everything_else))

        # Show key points about Whirlpools
        notes = VGroup(
            Text("Key Innovations of Whirlpools:", font_size=32, color=BLUE),
            Text("• Standardized tick array system", font_size=28),
            Text("• Optimized for Solana's architecture", font_size=28),
            Text("• More efficient position management", font_size=28),
            Text("• Lower gas costs through batching", font_size=28),
            Text("• Better liquidity utilization", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(2)

        # Show technical details
        self.play(FadeOut(notes))
        
        technical = VGroup(
            Text("How Whirlpools Work:", font_size=32, color=BLUE),
            Text("1. Divides price range into tick arrays", font_size=28),
            Text("2. Groups similar positions together", font_size=28),
            Text("3. Optimizes updates and rebalancing", font_size=28),
            Text("4. Reduces computational overhead", font_size=28),
            Text("5. Maintains price precision", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        technical.move_to(ORIGIN)

        self.play(Write(technical))
        self.wait(3)

        # Add comparison with other models
        self.play(FadeOut(technical))
        
        comparison = VGroup(
            Text("Advantages over Traditional CLMMs:", font_size=32, color=BLUE),
            Text("Cost Efficiency:", font_size=28),
            Text("• Lower transaction costs", font_size=24),
            Text("• Reduced computational overhead", font_size=24),
            Text("User Experience:", font_size=28),
            Text("• Simpler position management", font_size=24),
            Text("• More predictable behavior", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        comparison.move_to(ORIGIN)

        self.play(Write(comparison))
        self.wait(3)