from IPython.display import HTML, display


class Submitter:
    @staticmethod
    def _show_message(message: str, color: str = "black") -> None:
        style = f"margin-left: 5px; color: {color}; font-family: monospace"
        display(HTML(f'<p style="{style}">{message}</p>'))
