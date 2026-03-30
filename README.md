# Bug Triage Tool (Python)

## Overview
Python-based tool to analyze and classify bug data with support for filtering, logging, and report generation. Designed to simulate a simplified JIRA-style bug triage workflow.

## Features
- Reads bug data from CSV and JSON files
- Classifies bugs by priority and severity
- Filters high-priority and critical issues
- Generates summary reports
- Logging for execution tracking and debugging
- Modular structure with separate components
- Basic unit tests for core functionality

## Project Structure
src/ → core logic (runner, reporter, utils)
tests/ → test cases
main.py → entry point

## How to Run
Run all tests:
python main.py
Run specific test:
python main.py --filter login

## Example Use Case
- Analyze incoming bug data  
- Identify critical issues quickly  
- Generate reports for debugging and tracking  
