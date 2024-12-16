from manim import *

class TCPVisualization(Scene):
    def construct(self):
        # Create title and initial explanation
        title = Text("TCP Connection Process", color=BLUE).scale(0.8)
        title.to_edge(UP)
        explanation = Text(
            "TCP ensures reliable, ordered data transmission",
            color=GRAY
        ).scale(0.4)
        explanation.next_to(title, DOWN)
        
        self.play(Write(title), Write(explanation))
        self.wait()
        
        # Create client and server with detailed labels
        client = Rectangle(height=2, width=3)
        client.to_edge(LEFT)
        client_text = Text("Client\nPort: 12345").scale(0.4).next_to(client, UP)
        
        server = Rectangle(height=2, width=3)
        server.to_edge(RIGHT)
        server_text = Text("Server\nPort: 80").scale(0.4).next_to(server, UP)
        
        endpoints = VGroup(client, server, client_text, server_text)
        
        self.play(
            Create(client),
            Create(server),
            Write(client_text),
            Write(server_text)
        )
        self.wait()
        
        # Three-way handshake explanation
        handshake_text = Text(
            "Three-Way Handshake Phase",
            color=BLUE
        ).scale(0.6)
        handshake_text.to_edge(UP)
        self.play(Transform(explanation, handshake_text))
        
        # Step 1: SYN
        syn_group = VGroup()
        syn_arrow = Arrow(
            start=client.get_right(),
            end=server.get_left(),
            buff=0.5,
            color=BLUE
        )
        syn_details = VGroup(
            Text("SYN", color=BLUE).scale(0.4),
            Text("Seq=0", color=BLUE_A).scale(0.3),
            Text("Control Bits: SYN=1", color=BLUE_B).scale(0.3)
        ).arrange(DOWN, buff=0.1)
        syn_details.next_to(syn_arrow, UP, buff=0.1)
        syn_group.add(syn_arrow, syn_details)
        
        self.play(
            Create(syn_arrow),
            Write(syn_details)
        )
        self.wait()
        
        # Step 2: SYN-ACK (fade out previous)
        self.play(FadeOut(syn_group))
        
        syn_ack_group = VGroup()
        syn_ack_arrow = Arrow(
            start=server.get_left(),
            end=client.get_right(),
            buff=0.5,
            color=GREEN
        )
        syn_ack_details = VGroup(
            Text("SYN-ACK", color=GREEN).scale(0.4),
            Text("Seq=5000, Ack=1", color=GREEN_A).scale(0.3),
            Text("Control Bits: SYN=1, ACK=1", color=GREEN_B).scale(0.3)
        ).arrange(DOWN, buff=0.1)
        syn_ack_details.next_to(syn_ack_arrow, UP, buff=0.1)
        syn_ack_group.add(syn_ack_arrow, syn_ack_details)
        
        self.play(
            Create(syn_ack_arrow),
            Write(syn_ack_details)
        )
        self.wait()
        
        # Step 3: ACK (fade out previous)
        self.play(FadeOut(syn_ack_group))
        
        ack_group = VGroup()
        ack_arrow = Arrow(
            start=client.get_right(),
            end=server.get_left(),
            buff=0.5,
            color=YELLOW
        )
        ack_details = VGroup(
            Text("ACK", color=YELLOW).scale(0.4),
            Text("Seq=1, Ack=5001", color=YELLOW_A).scale(0.3),
            Text("Control Bits: ACK=1", color=YELLOW_B).scale(0.3)
        ).arrange(DOWN, buff=0.1)
        ack_details.next_to(ack_arrow, UP, buff=0.1)
        ack_group.add(ack_arrow, ack_details)
        
        self.play(
            Create(ack_arrow),
            Write(ack_details)
        )
        self.wait()
        
        # Clear handshake and show connection established
        self.play(FadeOut(ack_group))
        
        connection_text = VGroup(
            Text("Connection Established", color=GREEN).scale(0.6),
            Text("Full-duplex connection ready for data transfer", color=GREEN_A).scale(0.4)
        ).arrange(DOWN, buff=0.1)
        connection_text.to_edge(UP)
        self.play(Transform(explanation, connection_text))
        self.wait()
        
        # Data segmentation visualization
        segmentation_text = Text(
            "Breaking Down Image Data into TCP Packets",
            color=RED
        ).scale(0.6)
        segmentation_text.to_edge(UP)
        self.play(Transform(explanation, segmentation_text))
        
        # Create image representation
        image_rect = Rectangle(height=3, width=4, color=BLUE)
        image_rect.move_to(ORIGIN)
        image_label = Text("image.jpg\n(400KB)", color=BLUE).scale(0.4)
        image_label.next_to(image_rect, UP)
        
        self.play(
            Create(image_rect),
            Write(image_label)
        )
        self.wait()
        
        # Segment into packets
        num_packets = 4
        packets = VGroup()
        packet_labels = VGroup()
        segments = VGroup()
        
        # Create packet rectangles and labels
        for i in range(num_packets):
            packet = Rectangle(height=0.6, width=0.8, color=RED)
            packet.next_to(image_rect, DOWN, buff=1.5)
            packet.shift(RIGHT * (i - num_packets/2 + 0.5) * 1.2)
            
            label = Text(f"Packet {i+1}\n(100KB)", color=RED).scale(0.3)
            label.next_to(packet, DOWN)
            
            packets.add(packet)
            packet_labels.add(label)
        
        # Animate breaking down image into packets
        for i in range(num_packets):
            segment = Rectangle(
                height=3,
                width=4/num_packets,
                color=RED,
                stroke_opacity=0.3,
                fill_opacity=0.2
            )
            segment.move_to(image_rect.get_left() + RIGHT * (i + 0.5) * 4/num_packets)
            segments.add(segment)
            
            self.play(
                Create(segment),
                Create(packets[i]),
                Write(packet_labels[i])
            )
        
        self.wait()
        
        # Clear segmentation visualization
        self.play(
            FadeOut(image_rect),
            FadeOut(image_label),
            FadeOut(packets),
            FadeOut(packet_labels),
            FadeOut(segments)
        )
        
        # Data transfer phase
        data_transfer_text = Text(
            "Data Transfer Phase",
            color=RED
        ).scale(0.6)
        data_transfer_text.to_edge(UP)
        self.play(Transform(explanation, data_transfer_text))
        
        # Data transfer with sequence numbers (one direction at a time)
        seq_num = 1
        for i in range(3):
            # Data packet (client to server)
            data_group = VGroup()
            data_arrow = Arrow(
                start=client.get_right(),
                end=server.get_left(),
                buff=0.5,
                color=RED
            )
            data_details = VGroup(
                Text(f"DATA Packet {i+1}", color=RED).scale(0.4),
                Text(f"Seq={seq_num}, Len=100", color=RED_A).scale(0.3),
                Text("PSH=1, ACK=1", color=RED_B).scale(0.3)
            ).arrange(DOWN, buff=0.1)
            data_details.next_to(data_arrow, UP, buff=0.1)
            data_group.add(data_arrow, data_details)
            
            self.play(
                Create(data_arrow),
                Write(data_details)
            )
            self.wait(0.5)
            
            # Clear data packet before showing ACK
            self.play(FadeOut(data_group))
            
            # ACK for data (server to client)
            ack_group = VGroup()
            ack_arrow = Arrow(
                start=server.get_left(),
                end=client.get_right(),
                buff=0.5,
                color=PURPLE
            )
            ack_details = VGroup(
                Text("ACK", color=PURPLE).scale(0.4),
                Text(f"Ack={seq_num + 100}", color=PURPLE_A).scale(0.3),
                Text("Window=1024", color=PURPLE_B).scale(0.3)
            ).arrange(DOWN, buff=0.1)
            ack_details.next_to(ack_arrow, UP, buff=0.1)
            ack_group.add(ack_arrow, ack_details)
            
            self.play(
                Create(ack_arrow),
                Write(ack_details)
            )
            self.wait(0.5)
            
            # Clear ACK before next packet
            self.play(FadeOut(ack_group))
            
            seq_num += 100
        
        # Connection termination phase
        termination_text = Text(
            "Connection Termination (Four-Way Handshake)",
            color=RED_E
        ).scale(0.6)
        termination_text.to_edge(UP)
        self.play(Transform(explanation, termination_text))
        
        # FIN from client
        fin_group = VGroup()
        fin_arrow = Arrow(
            start=client.get_right(),
            end=server.get_left(),
            buff=0.5,
            color=RED_E
        )
        fin_details = VGroup(
            Text("FIN", color=RED_E).scale(0.4),
            Text("Seq=301, FIN=1", color=RED_E).scale(0.3),
            Text("Control Bits: FIN=1", color=RED_E).scale(0.3)
        ).arrange(DOWN, buff=0.1)
        fin_details.next_to(fin_arrow, UP, buff=0.1)
        fin_group.add(fin_arrow, fin_details)
        
        self.play(
            Create(fin_arrow),
            Write(fin_details)
        )
        self.wait()
        
        # Clear FIN before ACK
        self.play(FadeOut(fin_group))
        
        # ACK from server
        final_ack_group = VGroup()
        final_ack_arrow = Arrow(
            start=server.get_left(),
            end=client.get_right(),
            buff=0.5,
            color=PURPLE_E
        )
        final_ack_details = VGroup(
            Text("ACK", color=PURPLE_E).scale(0.4),
            Text("Ack=302", color=PURPLE_E).scale(0.3),
            Text("Control Bits: ACK=1", color=PURPLE_E).scale(0.3)
        ).arrange(DOWN, buff=0.1)
        final_ack_details.next_to(final_ack_arrow, UP, buff=0.1)
        final_ack_group.add(final_ack_arrow, final_ack_details)
        
        self.play(
            Create(final_ack_arrow),
            Write(final_ack_details)
        )
        self.wait()
        
        # Clear final ACK
        self.play(FadeOut(final_ack_group))
        
        # Connection closed text
        closed_text = VGroup(
            Text("Connection Closed", color=RED).scale(0.6),
            Text("All resources released", color=RED_A).scale(0.4)
        ).arrange(DOWN, buff=0.1)
        closed_text.to_edge(UP)
        self.play(Transform(explanation, closed_text))
        self.wait(2)
        
# manim -pql tcp.py TCPVisualization