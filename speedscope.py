# speedscope.py

from rich.console import Console
from rich.table import Table
import speedtest

console = Console()

def run_speedtest():
    console.print("[bold cyan]🚀 Running SpeedScope...[/bold cyan]\n")
    
    st = speedtest.Speedtest()
    st.get_best_server()

    download = st.download() / 1_000_000  # bits to Mbps
    upload = st.upload() / 1_000_000
    ping = st.results.ping
    server = st.get_best_server()

    table = Table(title="🌐 SpeedScope Network Stats")

    table.add_column("Metric", style="cyan", justify="right")
    table.add_column("Value", style="magenta")

    table.add_row("Ping", f"{ping:.2f} ms")
    table.add_row("Download", f"{download:.2f} Mbps")
    table.add_row("Upload", f"{upload:.2f} Mbps")
    table.add_row("ISP", st.results.client['isp'])
    table.add_row("Server", f"{server['sponsor']} - {server['name']}")

    console.print(table)

if __name__ == "__main__":
    run_speedtest()

