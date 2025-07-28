# MCP Server for Starters

A simple Model Context Protocol (MCP) server implementation that provides basic utility tools. Perfect for beginners learning MCP development!

## 🚀 Features

This MCP server provides 4 useful tools:

1. **Echo Tool** - Repeats your text back
2. **Calculator Tool** - Performs basic arithmetic calculations
3. **Reverse Text Tool** - Flips text backwards
4. **Weather Tool** - Gets weather information for Vietnamese cities

## � Requirements

- Python 3.8+
- `mcp` library

## 🛠️ Installation

1. Clone this repository:
```bash
git clone https://github.com/DangLam2603/mcp-server-for-starters.git
cd mcp-server-for-starters
```

2. Install dependencies:
```bash
pip install mcp
```

## 🎯 Usage

### Standalone Testing
```bash
python my_mcp_server.py
```

### Integration with Kiro IDE

Add this configuration to your `.kiro/settings/mcp.json`:

```json
{
    "mcpServers": {
        "my-mcp-server": {
            "command": "python",
            "args": ["path/to/my_mcp_server.py"],
            "cwd": "path/to/project",
            "env": {},
            "disabled": false,
            "autoApprove": ["echo", "reverse_text"]
        }
    }
}
```

## 🔧 Available Tools

### 1. Echo Tool
```python
# Example usage
echo("Hello World!")
# Output: "Echo: Hello World!"
```

### 2. Calculator Tool
```python
# Example usage
calculate("2 + 3 * 4")
# Output: "Result: 14"
```

### 3. Reverse Text Tool
```python
# Example usage
reverse_text("Hello World")
# Output: "Reversed: dlroW olleH"
```

### 4. Weather Tool
```python
# Example usage
caculate_tempurature("Hanoi")
# Output: "Weather in Hanoi: 28°C, Partly cloudy, Humidity: 75%"
```

Supported cities: Hanoi, Ho Chi Minh, Da Nang, Hue, Can Tho

## 📁 Project Structure

```
mcp-server-for-starters/
├── my_mcp_server.py      # Main MCP server implementation
├── pyproject.toml        # Project configuration
├── test_mcp_server.py    # Test script (if available)
└── README.md            # This file
```

## 🧪 Testing

You can test the server functionality by running the included test script:

```bash
python test_mcp_server.py
```

## 🤝 Contributing

This is a beginner-friendly project! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Add new tools or improve existing ones
4. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🎓 Learning Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Kiro IDE MCP Integration](https://docs.kiro.ai/)

## 🐛 Issues

If you encounter any issues, please create an issue on GitHub with:
- Your operating system
- Python version
- Error message (if any)
- Steps to reproduce

---

**Happy coding! 🎉**