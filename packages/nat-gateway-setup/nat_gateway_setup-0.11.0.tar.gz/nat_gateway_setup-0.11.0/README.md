# NAT Configurator

NAT Configurator is a CLI tool designed to set up a Linux machine as a network gateway or router. By providing Network Address Translation (NAT) services to another network interface, the Linux machine can enable internet access for devices connected to this interface, effectively creating a network behind a gateway.

This is useful for scenarios where you have a set of devices connected to a local network and you want to manage their internet access through a single point. For instance, it can be used in a home network setup where the Linux machine is a central router connecting multiple devices to the internet.

## Installation

This package is published on PyPI. You can install it using pip:

```bash
pip install nat-configurator
```

Alternatively, you can clone the repository and use poetry to build and install the package:

```bash
git clone https://github.com/your-github-username/nat-configurator.git
cd nat-configurator
poetry build
pip install dist/nat_configurator-0.1.0-py3-none-any.whl  # replace with actual filename
```

**Note:** You might need to run it with `sudo` if you encounter permission errors. This setup process involves configuring the network interface, dnsmasq, and firewall settings. Ensure to backup any existing configurations as this tool will overwrite them.

## Usage

You can provide the required information as command line arguments:

```bash
sudo nat-configurator --ip <ip> --netmask <netmask> --dhcp-start-ip <start_ip> --dhcp-ip-count <ip_count> --wlan <wlan_interface> --lan <lan_interface>
```

- `--ip`: The IP address to use for the NAT gateway.
- `--netmask`: The netmask for the network.
- `--dhcp-start-ip`: The start IP of the DHCP range.
- `--dhcp-ip-count`: The number of IPs in the DHCP range.
- `--wlan`: The incoming network interface (e.g., your WiFi interface).
- `--lan`: The local network interface (e.g., your Ethernet interface).

If arguments are not provided via command line, the tool will prompt the user to enter the required information interactively.

```bash
sudo nat-configurator
```

The tool also checks for and installs necessary dependencies, checks the firewall conditions, enables IP forwarding, configures the network interface, and sets up DNSMasq and firewall.

## Security Considerations

While setting up a Linux machine as a network gateway or router using NAT is a common practice and can simplify network management, it also comes with its own set of security implications that you need to consider. Here are a few:

1. **Single Point of Failure:** The Linux machine acting as the NAT gateway becomes a single point of failure in your network setup. If it goes down or gets compromised, all devices using it for internet access may lose connectivity or risk exposure to threats.

2. **Internal Threats:** If a device on the local network behind the NAT gateway is compromised, it can pose a threat to other devices on the same network. Since these devices are typically trusted, the compromised device could potentially launch attacks on other local devices or on the gateway itself.

3. **Security of the NAT Gateway:** The security of your NAT gateway is paramount. Ensure it is well-protected against external threats. Keep the system updated, use strong passwords, limit SSH access, and implement necessary firewall rules.

4. **Limited Isolation:** While NAT does provide a certain level of isolation between the local network and the internet, it should not be solely relied upon for security. Consider employing additional security measures such as firewalls, IDS/IPS, and regular system audits.

5. **Egress Filtering:** NAT allows outbound connections from devices on the local network. If one of these devices becomes infected with malware, it could potentially use the NAT gateway to communicate with an external command and control server. Implementing egress filtering rules on the NAT gateway can help mitigate this risk.

This tool is designed to facilitate setting up a NAT gateway, but it's crucial to remember that security is an ongoing process. Always follow the best security practices and keep your systems updated.

