from ip_utils import ip_to_binary, get_network_prefix

class Router:
    def __init__(self, routes):
        self.forwarding_table = []
        self.build_forwarding_table(routes)

    def build_forwarding_table(self, routes):
        """Convert CIDR routes to binary prefixes and sort by prefix length."""
        table = []
        for cidr, link in routes:
            prefix = get_network_prefix(cidr)
            table.append((prefix, link))
        self.forwarding_table = sorted(table, key=lambda x: len(x[0]), reverse=True)

    def route_packet(self, dest_ip: str) -> str:
        """Implement Longest Prefix Matching algorithm."""
        binary_ip = ip_to_binary(dest_ip)
        for prefix, link in self.forwarding_table:
            if binary_ip.startswith(prefix):
                return link
        return "Default Gateway"


if __name__ == "__main__":
    routes = [
        ("223.1.1.0/24", "Link 0"),
        ("223.1.2.0/24", "Link 1"),
        ("223.1.3.0/24", "Link 2"),
        ("223.1.0.0/16", "Link 4 (ISP)")
    ]

    router = Router(routes)

    print(router.route_packet("223.1.1.100"))  # Link 0
    print(router.route_packet("223.1.2.5"))    # Link 1
    print(router.route_packet("223.1.250.1"))  # Link 4 (ISP)
    print(router.route_packet("198.51.100.1")) # Default Gateway
