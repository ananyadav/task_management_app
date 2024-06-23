Task Management Application Documentation

Repository link: https://github.com/ananyadav/task_management_app.git
Project Overview
The Task Management Application is a web-based tool designed to help users manage their tasks effectively. It allows users to add, edit, delete tasks, mark tasks as completed, and view a list of their tasks. The application uses HTML, CSS for styling, Bootstrap for UI components, and JavaScript (with Fetch API) for dynamic interaction with a server-side API.
Files and Directory Structure
The project consists of the following files and directories:
1.	index.html - The main HTML file containing the application's structure and layout.
2.	style.css - Custom CSS file for styling the application beyond Bootstrap's default styles.
3.	script.js - JavaScript file for client-side functionality, including adding tasks, fetching tasks from the server, editing tasks, and managing UI interactions.
4.	server.py - Python file serving as a mock backend server using Flask. It includes endpoints /tasks, /add_task, /edit_task, and /delete_task to handle CRUD operations for tasks.
5.	README.md - Documentation file that provides an overview of the project, setup instructions, and any additional notes.
6.	Design Notes - Document explaining design choices, challenges faced, and future improvements.
Design Choices and Features
•	Responsive Design: Bootstrap is used for responsive layout and components, ensuring the application works well across different screen sizes.
•	Sidebar Navigation: Implemented a sidebar toggle button to show/hide the task list, providing a cleaner user interface.
•	Modal for Editing: Utilized Bootstrap modal for editing tasks, enhancing user experience by providing a focused editing environment without leaving the main task list view.
•	Checkbox for Task Completion: Included a checkbox to mark tasks as completed or pending, enhancing task management capabilities.
Challenges Faced
•	Integration with Backend: Setting up the Flask server and ensuring proper communication between the frontend and backend posed initial challenges, especially with handling CORS (Cross-Origin Resource Sharing) issues during development.
•	Data Synchronization: Ensuring synchronization between frontend UI updates and backend data changes required careful handling, especially when adding, editing, or deleting tasks.
•	UI/UX Design: Striking a balance between functionality and simplicity in UI design while maintaining responsiveness across devices was a recurring challenge.
Future Improvements
•	User Authentication: Implementing user authentication to secure tasks and allow users to have personalized task lists.
•	Sorting and Filtering: Adding options to sort tasks by priority, due date, or category, and filtering tasks based on completion status or other criteria.
•	Notifications: Incorporating notifications for task deadlines, reminders, or updates.
•	Collaboration Features: Enabling collaboration by allowing task sharing or assignment among users.
•	Data Persistence: Enhancing the backend to use a database for persistent storage of tasks and user data.
Conclusion
The Task Management Application provides a foundational platform for managing tasks efficiently. It leverages modern web technologies to deliver a responsive and intuitive user experience. Future enhancements will focus on adding more advanced features to cater to diverse user needs and improving overall performance and usability.


