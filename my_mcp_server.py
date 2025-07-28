#!/usr/bin/env python3
"""
Simple MCP Server - Easy to understand!

This server provides 3 basic tools:
1. Echo - repeats your text back
2. Calculate - does math for you  
3. Reverse - flips your text backwards
"""

import asyncio
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio

# Create our server
server = Server("my-mcp-server")

# STEP 1: Tell clients what tools we have
@server.list_tools()
async def get_available_tools():
    """Returns a list of tools that clients can use"""
    
    # Tool 1: Echo tool
    echo_tool = types.Tool(
        name="echo",
        description="Echo back the provided text",
        inputSchema={
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Text to echo back"}
            },
            "required": ["text"]
        }
    )
    
    # Tool 2: Calculator tool
    calculator_tool = types.Tool(
        name="calculate", 
        description="Perform basic arithmetic calculations",
        inputSchema={
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "Math expression like '2 + 3 * 4'"}
            },
            "required": ["expression"]
        }
    )
    
    # Tool 3: Text reverser tool
    reverse_tool = types.Tool(
        name="reverse_text",
        description="Reverse the provided text", 
        inputSchema={
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Text to reverse"}
            },
            "required": ["text"]
        }
    )
    # Tool 4: Weather tool
    weather_tool = types.Tool(
        name="caculate_tempurature",
        description="Get weather information for a city",
        inputSchema={
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "City name to get weather for"}
            },
            "required": ["text"]
        }
    )
    
    return [echo_tool, calculator_tool, reverse_tool, weather_tool]

# STEP 2: Actually run the tools when requested
@server.call_tool()
async def run_tool(tool_name: str, tool_arguments: dict):
    """This function runs when someone wants to use a tool"""
    
    # Make sure we have arguments
    if tool_arguments is None:
        tool_arguments = {}
    
    # ECHO TOOL: Just repeat the text back
    if tool_name == "echo":
        user_text = tool_arguments.get("text", "")
        response = f"Echo: {user_text}"
        return [types.TextContent(type="text", text=response)]
    
    # CALCULATOR TOOL: Do math
    elif tool_name == "calculate":
        math_expression = tool_arguments.get("expression", "")
        try:
            # Calculate the result
            answer = eval(math_expression)  # Note: eval() can be dangerous in real apps
            response = f"Result: {answer}"
            return [types.TextContent(type="text", text=response)]
        except Exception as error:
            response = f"Error: {str(error)}"
            return [types.TextContent(type="text", text=response)]
    
    # REVERSE TOOL: Flip text backwards
    elif tool_name == "reverse_text":
        user_text = tool_arguments.get("text", "")
        flipped_text = user_text[::-1]  # Python magic to reverse text
        response = f"Reversed: {flipped_text}"
        return [types.TextContent(type="text", text=response)]
    # WEATHER TOOL: Get weather for a city
    elif tool_name == "caculate_tempurature":
        city = tool_arguments.get("text", "").lower()
        
        # Simple weather simulation based on city
        weather_data = {
            "hanoi": {"temp": 28, "condition": "Partly cloudy", "humidity": 75},
            "ho chi minh": {"temp": 32, "condition": "Sunny", "humidity": 80},
            "da nang": {"temp": 30, "condition": "Clear", "humidity": 70},
            "hue": {"temp": 26, "condition": "Overcast", "humidity": 85},
            "can tho": {"temp": 31, "condition": "Humid", "humidity": 90},
            "default": {"temp": 25, "condition": "Unknown", "humidity": 60}
        }
        
        # Get weather for the city or use default
        weather = weather_data.get(city, weather_data["default"])
        
        response = f"Weather in {city.title()}: {weather['temp']}°C, {weather['condition']}, Humidity: {weather['humidity']}%"
        return [types.TextContent(type="text", text=response)]
    # Unknown tool
    else:
        raise ValueError(f"I don't know how to use tool: {tool_name}")

# STEP 3: Start the server
async def start_server():
    """Start the MCP server and keep it running"""
    
    # Create communication channels
    async with mcp.server.stdio.stdio_server() as (input_stream, output_stream):
        
        # Configure server settings
        server_config = InitializationOptions(
            server_name="my-mcp-server",
            server_version="0.1.0", 
            capabilities=server.get_capabilities(
                notification_options=NotificationOptions(),
                experimental_capabilities={}
            )
        )
        
        # Start the server (this runs forever until stopped)
        await server.run(input_stream, output_stream, server_config)

# Run the server when this file is executed
if __name__ == "__main__":
    print("Starting MCP Server...")
    print("Server will run until you stop it (Ctrl+C)")
    asyncio.run(start_server())