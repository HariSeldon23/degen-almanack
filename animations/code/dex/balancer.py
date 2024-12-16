from manim import *
import numpy as np

class BalancerWeightedPool(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.0f}".format(num)

        # Initial pool values for an 80/20 ETH/USDC pool at $3,500 ETH
        # We'll use higher ETH and lower USDC to demonstrate weight impact
        eth_weight = 0.8
        usdc_weight = 0.2
        initial_eth = 100
        initial_usdc = 70_000  # Reduced USDC due to 20% weight
        
        # Value function for weighted constant product
        def get_y(x):
            # (x₁^w₁ * x₂^w₂) = k
            # For our case: (eth^0.8 * usdc^0.2) = k
            k = (initial_eth ** eth_weight) * (initial_usdc ** usdc_weight)
            # Solve for y (USDC) given x (ETH)
            try:
                return (k / (x ** eth_weight)) ** (1 / usdc_weight)
            except:
                return 0

        # Create title and formula
        title = Text("Balancer Weighted Pool Formula", font_size=36)
        subtitle = Text("(x₁^W₁ × x₂^W₂) = k", font_size=32, color=BLUE)
        weights = Text("Weights: 80% ETH, 20% USDC", font_size=28, color=GREEN)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)
        weights.next_to(subtitle, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(Write(weights))
        self.wait(1)

        # Show initial pool state
        initial_state = VGroup(
            Text("Initial Pool State:", font_size=24),
            Text(f"ETH: {initial_eth} (80% weight)", font_size=24),
            Text(f"USDC: {format_number(initial_usdc)} (20% weight)", font_size=24),
            Text(f"ETH Price: ~${format_number(initial_usdc/initial_eth)}", font_size=24),
            Text("Higher ETH weight = Higher ETH ratio", font_size=24, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT)
        initial_state.to_edge(LEFT).shift(UP)

        self.play(Write(initial_state))
        self.wait(1)

        # Create coordinate system
        axes = Axes(
            x_range=[0, 200, 50],
            y_range=[0, 200_000, 50_000],
            x_length=6,
            y_length=5,
            tips=False,
            axis_config={
                "include_numbers": False
            }
        ).shift(DOWN * 0.5)

        # Add custom axis labels
        x_label = Text("ETH (80%)", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("USDC (20%)", font_size=24).next_to(axes.y_axis, UP)
        
        # Add axis values
        x_values = VGroup()
        for x in [0, 50, 100, 150, 200]:
            label = Text(str(x), font_size=16)
            label.next_to(axes.c2p(x, 0), DOWN)
            x_values.add(label)

        y_values = VGroup()
        for y in [0, 50_000, 100_000, 150_000, 200_000]:
            label = Text(format_number(y), font_size=16)
            label.next_to(axes.c2p(0, y), LEFT)
            y_values.add(label)

        # Create the weighted curve
        curve = axes.plot(
            get_y,
            x_range=[0.1, 200],
            color=BLUE,
        )

        # Show the axes and curve
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(x_values),
            Write(y_values)
        )
        self.play(Create(curve))
        
        # Show current pool position
        current_dot = Dot(axes.c2p(initial_eth, initial_usdc), color=GREEN)
        current_label = Text("Current", font_size=20).next_to(current_dot, RIGHT)
        
        self.play(
            Create(current_dot),
            Write(current_label)
        )

        # Demonstrate a trade
        trade_size = 20
        new_eth = initial_eth - trade_size
        new_usdc = get_y(new_eth)

        trade_info = VGroup(
            Text("Sell 20 ETH:", font_size=24),
            Text(f"New ETH: {format_number(new_eth)}", font_size=24),
            Text(f"New USDC: {format_number(new_usdc)}", font_size=24),
            Text("Notice higher price impact due to weights!", font_size=24, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT)
        trade_info.next_to(initial_state, DOWN, buff=1)

        self.play(Write(trade_info))

        # Show trade movement
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
            Text(f"Start: ${format_number(initial_price)}/ETH", font_size=20),
            Text(f"End: ${format_number(final_price)}/ETH", font_size=20),
            Text("Higher weight = Higher impact", font_size=20, color=BLUE)
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
            Text("• Weights determine the desired token ratio", font_size=28),
            Text("• Higher weight = More of that token in pool", font_size=28),
            Text("• Price impact varies with token weights", font_size=28),
            Text("• Supports any number of tokens with custom weights", font_size=28),
            Text("• Common uses: Index funds, Risk-adjusted pools", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(3)