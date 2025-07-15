# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a TDD-driven web application development project designed to test how Test-Driven Development can improve AI coding reliability. The project follows a strict 10-milestone approach where each milestone has clear pass/fail criteria that must be met before proceeding.

## Architecture

- **Backend**: Python HTTP server (`app.py`) serving both static files and API endpoints
- **Frontend**: Single HTML page (`index.html`) with JavaScript for user interaction
- **Communication**: HTTP requests between frontend and backend
- **Port**: Development server runs on localhost:8000

## Development Environment

### Virtual Environment
Always activate the Python virtual environment before working:
```bash
source venv/bin/activate
```

### Running the Application
```bash
python app.py
```
Then navigate to http://localhost:8000

### Testing Approach
Each milestone has a specific test that must pass before proceeding:
1. Manual testing through browser interaction
2. HTTP endpoint verification (GET/POST requests)
3. Error condition testing
4. Performance validation

## Project Milestones

The project follows 10 progressive milestones:

1. **Local Development Setup** - Basic server + HTML with button
2. **Backend Foundation** - API endpoint returning JSON
3. **Frontend Connection** - JavaScript request handling
4. **End-to-End Local Test** - Complete request/response cycle
5. **Error Handling** - Graceful failure management
6. **Data Processing** - Input validation and formatting
7. **UI Enhancement** - Loading states and interaction polish
8. **Deployment Preparation** - Production configuration
9. **Live Deployment** - Production deployment
10. **Production Validation** - Full acceptance testing

## Development Rules

- **Always use virtual environment**: Run `source venv/bin/activate` before any Python work
- **Use MCP servers**: Context7 for documentation, GitHub MCP for version control
- **Strict TDD**: Each milestone must pass its test before proceeding to the next
- **No jumping ahead**: Complete milestones in order
- **Clear pass/fail criteria**: Each test has measurable success conditions
- **Commit each milestone**: After test passes, commit milestone to GitHub before proceeding
- **Iterative refinement**: Build on previous milestones without breaking them
- **Documentation and Submission**: 
  * Always use MCP servers (Context7) for documentation references
  * Submit each completed milestone to GitHub after definitive test completion

## File Structure (Target)
```
/
├── app.py              # Python HTTP server
├── index.html          # Frontend interface
├── static/             # Static assets (if needed)
├── venv/              # Python virtual environment
└── CLAUDE.md          # This file
```

## Key Dependencies

Uses Python standard library only (http.server, socketserver) to minimize complexity and focus on TDD methodology.

## Testing Commands

Manual testing is performed by:
- Running the server and checking browser functionality
- Using browser developer tools to verify network requests
- Testing error conditions by stopping the server
- Validating response times and user experience

## Notes for Future Development

- Each milestone builds incrementally on the previous one
- Tests must be reproducible and have clear success/failure criteria
- Focus is on proving TDD methodology effectiveness, not complex functionality
- Use Context7 MCP server for documentation/library references when needed