from manim import *
import numpy as np

class LiquidityBookExplainer(Scene):
    def construct(self):
        def format_number(num):
            return "{:,.0f}".format(num)

        # Create title and introduction
        title = Text("Trader Joe's Liquidity Book (JOE v2)", font_size=36)
        subtitle = Text("Binned Liquidity Model", font_size=32, color=BLUE)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)

        # Initial explanation of bins vs continuous
        concept = VGroup(
            Text("Traditional Concentrated Liquidity:", font_size=24),
            Text("• Any arbitrary price range", font_size=24),
            Text("• Complex position management", font_size=24),
            Text("Liquidity Book Innovation:", font_size=24),
            Text("• Predefined price bins", font_size=24),
            Text("• Simpler to understand and use", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        concept.to_edge(LEFT).shift(UP)

        self.play(Write(concept))
        self.wait(1)

        # Create coordinate system for price bins
        axes = Axes(
            x_range=[2000, 4000, 200],
            y_range=[0, 1, 0.2],
            x_length=8,
            y_length=4,
            tips=False,
            axis_config={"include_numbers": False}
        ).shift(DOWN * 0.5)

        x_label = Text("ETH Price in USDC", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Liquidity Depth", font_size=24).next_to(axes.y_axis, UP)
        
        # Add price labels
        x_values = VGroup()
        for x in range(2000, 4001, 400):
            label = Text(f"${x}", font_size=16)
            label.next_to(axes.c2p(x, 0), DOWN)
            x_values.add(label)

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(x_values)
        )

        # Create bins for different price ranges
        bin_width = 200  # Width of each bin in USDC
        bins = []
        bin_labels = []
        
        # Create bins with varying heights to show liquidity concentration
        for price in range(2400, 3801, bin_width):
            # Make bins near current price (3000) taller
            height = 0.8 * np.exp(-0.0005 * abs(price - 3000))
            
            points = [
                axes.c2p(price, 0),
                axes.c2p(price, height),
                axes.c2p(price + bin_width, height),
                axes.c2p(price + bin_width, 0)
            ]
            bin_rect = Polygon(*points, fill_opacity=0.4, 
                             fill_color=BLUE if price == 3000 else GREEN,
                             color=BLUE if price == 3000 else GREEN)
            bins.append(bin_rect)
            
            # Add label for bin range
            if price in [2600, 3000, 3400]:  # Only label some bins for clarity
                label = Text(f"${price}-${price+bin_width}", font_size=16)
                label.next_to(bin_rect, UP)
                bin_labels.append(label)

        # Show bins one by one
        self.play(AnimationGroup(*[Create(bin) for bin in bins], lag_ratio=0.1))
        self.play(AnimationGroup(*[Write(label) for label in bin_labels]))

        # Add explanation of current price bin
        current_price_info = VGroup(
            Text("Current Price Bin", font_size=24, color=BLUE),
            Text("$3000-$3200", font_size=24),
            Text("Highest liquidity concentration", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        current_price_info.to_edge(RIGHT).shift(UP)

        self.play(Write(current_price_info))
        self.wait(1)

        # Fade out everything for key points
        everything_else = VGroup(
            axes, x_label, y_label, x_values, *bins, *bin_labels,
            concept, current_price_info
        )
        self.play(FadeOut(everything_else))

        # Show key points about Liquidity Book
        notes = VGroup(
            Text("Key Advantages of Liquidity Book:", font_size=32, color=BLUE),
            Text("• Predefined bins make position management simpler", font_size=28),
            Text("• Lower gas costs due to discrete price levels", font_size=28),
            Text("• Easy to understand where liquidity is concentrated", font_size=28),
            Text("• Multiple LPs can easily share the same bin", font_size=28),
            Text("• Reduced risk of liquidity fragmentation", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        notes.move_to(ORIGIN)

        self.play(Write(notes))
        self.wait(2)

        # Add comparison with other models
        self.play(FadeOut(notes))
        
        comparison = VGroup(
            Text("Comparison with Other DEXs:", font_size=32, color=BLUE),
            Text("vs Uniswap V2:", font_size=28),
            Text("• Much better capital efficiency", font_size=24),
            Text("vs Uniswap V3:", font_size=28),
            Text("• Simpler to use and understand", font_size=24),
            Text("• Lower gas costs", font_size=24),
            Text("• More predictable liquidity distribution", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        comparison.move_to(ORIGIN)

        self.play(Write(comparison))
        self.wait(3)

        # Add practical usage section
        self.play(FadeOut(comparison))
        
        usage = VGroup(
            Text("Practical Benefits:", font_size=32, color=BLUE),
            Text("For Liquidity Providers:", font_size=28),
            Text("• Easier to choose price ranges", font_size=24),
            Text("• Lower risk of position fragmentation", font_size=24),
            Text("For Traders:", font_size=28),
            Text("• More consistent liquidity depth", font_size=24),
            Text("• Better gas efficiency", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        usage.move_to(ORIGIN)

        self.play(Write(usage))
        self.wait(3)