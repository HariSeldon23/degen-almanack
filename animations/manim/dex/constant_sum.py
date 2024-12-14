from manim import *

class ConstantSumExplainer(Scene):
    def construct(self):
        # Helper function to format large numbers with commas
        def format_number(num):
            return "{:,.0f}".format(num)

        # Initial pool values - using same $3,500 ETH price for comparison
        initial_eth = 100
        initial_usdc = 350_000  # 100 ETH × $3,500
        k = initial_eth * 3500  # Total value in USDC terms

        # Create title with Text instead of Tex
        title = Text("The AMM Constant Sum Formula (Linear AMM)", font_size=36)
        formula = Text("x + y/3500 = k", font_size=32, color=BLUE)  # Normalized to ETH units
        
        title.to_edge(UP)
        formula.next_to(title, DOWN)

        # Create coordinate system
        axes = Axes(
            x_range=[0, 200, 50],
            y_range=[0, 700_000, 100_000],
            x_length=6,
            y_length=5,
            tips=False,
            axis_config={
                "include_numbers": False
            }
        ).shift(DOWN * 0.5)

        # Add custom axis labels
        x_label = Text("ETH", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("USDC", font_size=24).next_to(axes.y_axis, UP)
        
        # Add axis value labels
        x_values = VGroup()
        for x in [0, 50, 100, 150, 200]:
            label = Text(str(x), font_size=16)
            label.next_to(axes.c2p(x, 0), DOWN)
            x_values.add(label)

        y_values = VGroup()
        for y in [0, 200_000, 400_000, 600_000]:
            label = Text(format_number(y), font_size=16)
            label.next_to(axes.c2p(0, y), LEFT)
            y_values.add(label)

        # Create the constant sum line
        def constant_sum(x):
            return (k - x) * 3500  # Convert to USDC terms
        
        line = axes.plot(
            constant_sum,
            x_range=[0, k],
            color=BLUE,
        )

        # Initial animations
        self.play(Write(title))
        self.play(Write(formula))
        self.wait(1)

        # Show initial pool state
        initial_state = VGroup(
            Text("Initial Pool:", font_size=24),
            Text(f"ETH: {initial_eth}", font_size=24),
            Text(f"USDC: {format_number(initial_usdc)}", font_size=24),
            Text(f"ETH Price: $3,500 (fixed)", font_size=24, color=RED),
            Text(f"Total Value: ${format_number(k * 3500)}", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        initial_state.to_edge(LEFT).shift(UP)

        self.play(Write(initial_state))
        self.wait(1)

        # Create and animate the coordinate system
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(x_values),
            Write(y_values)
        )

        # Animate the line
        self.play(Create(line))
        self.wait(1)

        # Show current pool position
        current_dot = Dot(axes.c2p(initial_eth, initial_usdc), color=GREEN)
        current_label = Text("Current", font_size=20).next_to(current_dot, RIGHT)
        
        self.play(
            Create(current_dot),
            Write(current_label)
        )

        # Demonstrate a trade - buying all ETH
        trade_size = initial_eth  # Buying all ETH
        new_eth = 0  # Pool is empty of ETH
        new_usdc = initial_usdc + (trade_size * 3500)  # Price stays constant at 3500

        trade_info = VGroup(
            Text("Buy ALL ETH:", font_size=24, color=RED),
            Text(f"New ETH: {new_eth}", font_size=24),
            Text(f"New USDC: {format_number(new_usdc)}", font_size=24),
            Text("Pool is drained of ETH!", font_size=24, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT)
        trade_info.next_to(initial_state, DOWN, buff=1)

        self.play(Write(trade_info))

        # Show trade movement on line
        trade_dot = Dot(axes.c2p(new_eth, new_usdc), color=RED)
        trade_arrow = Arrow(
            start=axes.c2p(initial_eth, initial_usdc),
            end=axes.c2p(new_eth, new_usdc),
            color=YELLOW
        )
        trade_label = Text("Pool Drained!", font_size=20, color=RED).next_to(trade_dot, RIGHT)

        self.play(Create(trade_arrow))
        self.play(
            Create(trade_dot),
            Write(trade_label)
        )

        # Show price comparison
        price_info = VGroup(
            Text("Price Analysis:", font_size=24, color=RED),
            Text("Initial Price: $3,500/ETH", font_size=20),
            Text("Final Price: $3,500/ETH", font_size=20),
            Text("Price stays constant!", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT)
        price_info.to_edge(RIGHT).shift(UP)

        self.play(Write(price_info))
        self.wait(1)

        # Fade out everything except title for key points
        everything_else = VGroup(
            axes, line, current_dot, current_label, trade_dot, trade_label,
            trade_arrow, initial_state, trade_info, price_info,
            x_label, y_label, x_values, y_values
        )
        self.play(FadeOut(everything_else))

        # Add centered key points
        notes = VGroup(
            Text("Key Points:", font_size=32, color=BLUE),
            Text("• Price remains constant regardless of trade size", font_size=28),
            Text("• Pool can be completely drained of one asset", font_size=28, color=RED),
            Text("• No price impact or slippage", font_size=28),
            Text("• Not practical for real AMMs due to drainage risk", font_size=28, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(3)