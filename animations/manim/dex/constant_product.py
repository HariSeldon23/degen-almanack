from manim import *

class ConstantProductExplainer(Scene):
    def construct(self):
        # Helper function to format large numbers with commas
        def format_number(num):
            return "{:,.0f}".format(num)

        # Initial pool values - adjusted for $3,500 ETH price
        initial_eth = 100
        initial_usdc = 350_000  # 100 ETH × $3,500
        k = initial_eth * initial_usdc

        # Create title with Text instead of Tex
        title = Text("The AMM Constant Product Formula (Uniswap V2)", font_size=36)
        formula = Text("x × y = k", font_size=32, color=BLUE)
        
        title.to_edge(UP)
        formula.next_to(title, DOWN)

        # Create coordinate system with minimal text dependencies
        axes = Axes(
            x_range=[0, 200, 50],
            y_range=[0, 700_000, 100_000],  # Adjusted for higher USDC range
            x_length=6,
            y_length=5,
            tips=False,
            axis_config={
                "include_numbers": False
            }
        ).shift(DOWN * 0.5)

        # Add custom axis labels using Text
        x_label = Text("ETH", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("USDC", font_size=24).next_to(axes.y_axis, UP)
        
        # Add some axis value labels manually
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

        # Create the constant product curve
        curve = axes.plot(
            lambda x: k/x if x > 0 else 0,
            x_range=[k/700_000, 200],
            color=BLUE,
        )

        # Initial animations
        self.play(Write(title))
        self.play(Write(formula))
        self.wait(1)

        # Show initial pool state with ETH price
        initial_state = VGroup(
            Text("Initial Pool:", font_size=24),
            Text(f"ETH: {initial_eth}", font_size=24),
            Text(f"USDC: {format_number(initial_usdc)}", font_size=24),
            Text(f"ETH Price: $3,500", font_size=24),
            Text(f"k = {format_number(k)}", font_size=24)
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

        # Animate the curve
        self.play(Create(curve))
        self.wait(1)

        # Show current pool position
        current_dot = Dot(axes.c2p(initial_eth, initial_usdc), color=GREEN)
        current_label = Text("Current", font_size=20).next_to(current_dot, RIGHT)
        
        self.play(
            Create(current_dot),
            Write(current_label)
        )

        # Demonstrate a trade - selling 20 ETH
        trade_size = 20
        new_eth = initial_eth - trade_size  # Now subtracting ETH (selling)
        new_usdc = k / new_eth

        trade_info = VGroup(
            Text("Sell 20 ETH:", font_size=24),
            Text(f"New ETH: {new_eth}", font_size=24),
            Text(f"New USDC: {format_number(new_usdc)}", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        trade_info.next_to(initial_state, DOWN, buff=1)

        self.play(Write(trade_info))

        # Show trade movement on curve
        trade_dot = Dot(axes.c2p(new_eth, new_usdc), color=RED)
        trade_arrow = Arrow(
            start=axes.c2p(initial_eth, initial_usdc),
            end=axes.c2p(new_eth, new_usdc),
            color=YELLOW
        )
        trade_label = Text("After Trade", font_size=20).next_to(trade_dot, RIGHT)

        self.play(Create(trade_arrow))
        self.play(
            Create(trade_dot),
            Write(trade_label)
        )

        # Show price impact
        initial_price = initial_usdc / initial_eth
        final_price = new_usdc / new_eth
        
        price_impact = VGroup(
            Text("Price Impact:", font_size=24, color=RED),
            Text(f"Start: {format_number(initial_price)} USDC/ETH", font_size=20),
            Text(f"End: {format_number(final_price)} USDC/ETH", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT)
        price_impact.to_edge(RIGHT).shift(UP)

        self.play(Write(price_impact))
        self.wait(1)

        # Fade out everything except title for key points
        everything_else = VGroup(
            axes, curve, current_dot, current_label, trade_dot, trade_label,
            trade_arrow, initial_state, trade_info, price_impact,
            x_label, y_label, x_values, y_values
        )
        self.play(FadeOut(everything_else))

        # Add centered key points
        notes = VGroup(
            Text("Key Points:", font_size=32, color=BLUE),
            Text("• The product (k) never changes", font_size=28),
            Text("• Bigger trades = Bigger price impact", font_size=28),
            Text("• Pool always maintains liquidity", font_size=28),
            Text("• Price automatically adjusts based on pool ratio", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(3)