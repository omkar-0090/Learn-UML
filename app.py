from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'uml-learning-platform-2024'

UML_CONTENT = {
    'use-case': {
        'title': 'Use Case Diagram',
        'description': {
            'what': 'A Use Case Diagram is a behavioral UML diagram that represents the functional requirements of a system. It shows the relationships between actors (users or external systems) and use cases (system functionalities). Use case diagrams provide a high-level view of what a system should do from an external perspective.',
            'why': 'Use case diagrams are essential in software engineering for capturing and communicating system requirements. They help stakeholders understand the system\'s functionality without getting into technical details. These diagrams are commonly used during the requirements gathering phase, in system documentation, and for validating that all user needs are met. They bridge the gap between business requirements and technical implementation.'
        },
        'notations': [
            {
                'name': 'Actor',
                'description': 'Represents a user or external system that interacts with the system. Actors initiate use cases and can be people, organizations, or other systems.',
                'svg': '<svg width="80" height="100" xmlns="http://www.w3.org/2000/svg"><circle cx="40" cy="20" r="12" fill="none" stroke="#1e60ff" stroke-width="2"/><line x1="40" y1="32" x2="40" y2="60" stroke="#1e60ff" stroke-width="2"/><line x1="40" y1="45" x2="20" y2="55" stroke="#1e60ff" stroke-width="2"/><line x1="40" y1="45" x2="60" y2="55" stroke="#1e60ff" stroke-width="2"/><line x1="40" y1="60" x2="20" y2="85" stroke="#1e60ff" stroke-width="2"/><line x1="40" y1="60" x2="60" y2="85" stroke="#1e60ff" stroke-width="2"/></svg>'
            },
            {
                'name': 'Use Case',
                'description': 'An oval representing a specific functionality or service the system provides. Each use case describes a goal that an actor wants to achieve.',
                'svg': '<svg width="140" height="70" xmlns="http://www.w3.org/2000/svg"><ellipse cx="70" cy="35" rx="65" ry="30" fill="none" stroke="#1e60ff" stroke-width="2"/><text x="70" y="40" text-anchor="middle" fill="#1e60ff" font-size="14">Use Case</text></svg>'
            },
            {
                'name': 'System Boundary',
                'description': 'A rectangle that defines the scope of the system. Everything inside the boundary is part of the system; everything outside is external.',
                'svg': '<svg width="200" height="150" xmlns="http://www.w3.org/2000/svg"><rect x="5" y="20" width="190" height="125" fill="none" stroke="#1e60ff" stroke-width="2"/><text x="10" y="15" fill="#1e60ff" font-size="12" font-weight="bold">System Name</text></svg>'
            },
            {
                'name': 'Association',
                'description': 'A solid line connecting an actor to a use case, showing that the actor participates in that use case.',
                'svg': '<svg width="150" height="40" xmlns="http://www.w3.org/2000/svg"><line x1="10" y1="20" x2="140" y2="20" stroke="#1e60ff" stroke-width="2"/></svg>'
            },
            {
                'name': 'Include Relationship',
                'description': 'A dashed arrow with &lt;&lt;include&gt;&gt; stereotype indicating that one use case always includes the behavior of another use case.',
                'svg': '<svg width="180" height="50" xmlns="http://www.w3.org/2000/svg"><defs><marker id="include-arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e60ff"/></marker></defs><line x1="10" y1="25" x2="160" y2="25" stroke="#1e60ff" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#include-arrow)"/><text x="90" y="15" text-anchor="middle" fill="#1e60ff" font-size="11">&lt;&lt;include&gt;&gt;</text></svg>'
            },
            {
                'name': 'Extend Relationship',
                'description': 'A dashed arrow with &lt;&lt;extend&gt;&gt; stereotype showing optional or conditional behavior that extends a base use case.',
                'svg': '<svg width="180" height="50" xmlns="http://www.w3.org/2000/svg"><defs><marker id="extend-arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e60ff"/></marker></defs><line x1="10" y1="25" x2="160" y2="25" stroke="#1e60ff" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#extend-arrow)"/><text x="90" y="15" text-anchor="middle" fill="#1e60ff" font-size="11">&lt;&lt;extend&gt;&gt;</text></svg>'
            },
            {
                'name': 'Generalization',
                'description': 'A solid line with a hollow triangle arrow indicating inheritance between actors or use cases, showing that one is a specialized version of another.',
                'svg': '<svg width="150" height="50" xmlns="http://www.w3.org/2000/svg"><defs><marker id="generalization-arrow" markerWidth="15" markerHeight="15" refX="12" refY="5" orient="auto"><path d="M0,0 L0,10 L10,5 z" fill="white" stroke="#1e60ff" stroke-width="2"/></marker></defs><line x1="10" y1="25" x2="140" y2="25" stroke="#1e60ff" stroke-width="2" marker-end="url(#generalization-arrow)"/></svg>'
            }
        ],
        'example': {
            'scenario': 'Online Shopping System',
            'description': 'This diagram shows a customer interacting with an online shopping system. The customer can browse products, add items to cart, and checkout. The checkout process includes payment processing (shown with include relationship). Premium members have additional privileges (shown with generalization).',
            'svg': '<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ex1-arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e60ff"/></marker><marker id="ex1-gen" markerWidth="15" markerHeight="15" refX="12" refY="5" orient="auto"><path d="M0,0 L0,10 L10,5 z" fill="white" stroke="#1e60ff" stroke-width="2"/></marker></defs><rect x="150" y="50" width="350" height="320" fill="none" stroke="#1e60ff" stroke-width="2"/><text x="160" y="45" fill="#1e60ff" font-size="14" font-weight="bold">Online Shopping System</text><circle cx="70" cy="100" r="15" fill="none" stroke="#1e60ff" stroke-width="2"/><line x1="70" y1="115" x2="70" y2="150" stroke="#1e60ff" stroke-width="2"/><line x1="70" y1="130" x2="50" y2="145" stroke="#1e60ff" stroke-width="2"/><line x1="70" y1="130" x2="90" y2="145" stroke="#1e60ff" stroke-width="2"/><line x1="70" y1="150" x2="50" y2="180" stroke="#1e60ff" stroke-width="2"/><line x1="70" y1="150" x2="90" y2="180" stroke="#1e60ff" stroke-width="2"/><text x="70" y="200" text-anchor="middle" fill="#1e60ff" font-size="12">Customer</text><circle cx="70" cy="280" r="15" fill="none" stroke="#1e60ff" stroke-width="2"/><line x1="70" y1="295" x2="70" y2="330" stroke="#1e60ff" stroke-width="2"/><line x1="70" y1="310" x2="50" y2="325" stroke="#1e60ff" stroke-width="2"/><line x1="70" y1="310" x2="90" y2="325" stroke="#1e60ff" stroke-width="2"/><line x1="70" y1="330" x2="50" y2="360" stroke="#1e60ff" stroke-width="2"/><line x1="70" y1="330" x2="90" y2="360" stroke="#1e60ff" stroke-width="2"/><text x="70" y="380" text-anchor="middle" fill="#1e60ff" font-size="12">Premium</text><line x1="70" y1="265" x2="70" y2="215" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex1-gen)"/><ellipse cx="280" cy="100" rx="70" ry="30" fill="none" stroke="#1e60ff" stroke-width="2"/><text x="280" y="105" text-anchor="middle" fill="#1e60ff" font-size="12">Browse Products</text><ellipse cx="280" cy="180" rx="70" ry="30" fill="none" stroke="#1e60ff" stroke-width="2"/><text x="280" y="185" text-anchor="middle" fill="#1e60ff" font-size="12">Add to Cart</text><ellipse cx="280" cy="260" rx="70" ry="30" fill="none" stroke="#1e60ff" stroke-width="2"/><text x="280" y="265" text-anchor="middle" fill="#1e60ff" font-size="12">Checkout</text><ellipse cx="430" cy="260" rx="60" ry="25" fill="none" stroke="#1e60ff" stroke-width="2"/><text x="430" y="265" text-anchor="middle" fill="#1e60ff" font-size="11">Process Payment</text><line x1="90" y1="140" x2="210" y2="100" stroke="#1e60ff" stroke-width="2"/><line x1="90" y1="150" x2="210" y2="180" stroke="#1e60ff" stroke-width="2"/><line x1="90" y1="160" x2="210" y2="260" stroke="#1e60ff" stroke-width="2"/><line x1="350" y1="260" x2="370" y2="260" stroke="#1e60ff" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#ex1-arrow)"/><text x="360" y="250" text-anchor="middle" fill="#1e60ff" font-size="10">&lt;&lt;include&gt;&gt;</text></svg>'
        }
    },
    'class': {
        'title': 'Class Diagram',
        'description': {
            'what': 'A Class Diagram is a structural UML diagram that shows the static structure of a system by displaying classes, their attributes, methods, and relationships between objects. It is the most commonly used UML diagram in object-oriented software development. Class diagrams provide a blueprint for implementing the system\'s code structure.',
            'why': 'Class diagrams are fundamental in object-oriented design and programming. They help developers visualize the system architecture before writing code, document the system structure, and communicate design decisions across teams. These diagrams are extensively used in database design, API development, and system refactoring. They ensure that relationships between classes are clearly defined and help identify potential design issues early in development.'
        },
        'notations': [
            {
                'name': 'Class',
                'description': 'A rectangle divided into three sections: class name (top), attributes (middle), and methods (bottom). The class is the blueprint for creating objects.',
                'svg': '<svg width="180" height="140" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="160" height="120" fill="none" stroke="#1e60ff" stroke-width="2"/><line x1="10" y1="45" x2="170" y2="45" stroke="#1e60ff" stroke-width="2"/><line x1="10" y1="90" x2="170" y2="90" stroke="#1e60ff" stroke-width="2"/><text x="90" y="32" text-anchor="middle" fill="#1e60ff" font-size="14" font-weight="bold">ClassName</text><text x="20" y="65" fill="#1e60ff" font-size="11">- attribute1: Type</text><text x="20" y="80" fill="#1e60ff" font-size="11">+ attribute2: Type</text><text x="20" y="110" fill="#1e60ff" font-size="11">+ method1()</text><text x="20" y="125" fill="#1e60ff" font-size="11">- method2(): Type</text></svg>'
            },
            {
                'name': 'Attributes',
                'description': 'Properties or data members of a class, shown with visibility modifiers: + (public), - (private), # (protected), ~ (package).',
                'svg': '<svg width="180" height="80" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="160" height="60" fill="#f0f7ff" stroke="#1e60ff" stroke-width="2"/><text x="20" y="30" fill="#1e60ff" font-size="12">- privateAttr: String</text><text x="20" y="48" fill="#1e60ff" font-size="12">+ publicAttr: int</text><text x="20" y="65" fill="#1e60ff" font-size="12"># protectedAttr: boolean</text></svg>'
            },
            {
                'name': 'Association',
                'description': 'A solid line representing a relationship between two classes where one class uses or interacts with another.',
                'svg': '<svg width="200" height="50" xmlns="http://www.w3.org/2000/svg"><line x1="20" y1="25" x2="180" y2="25" stroke="#1e60ff" stroke-width="2"/><text x="10" y="15" fill="#1e60ff" font-size="11">1</text><text x="175" y="15" fill="#1e60ff" font-size="11">*</text></svg>'
            },
            {
                'name': 'Aggregation',
                'description': 'A "has-a" relationship shown with a hollow diamond, indicating that one class contains another but both can exist independently (shared ownership).',
                'svg': '<svg width="200" height="50" xmlns="http://www.w3.org/2000/svg"><line x1="50" y1="25" x2="180" y2="25" stroke="#1e60ff" stroke-width="2"/><path d="M20,25 L35,15 L50,25 L35,35 Z" fill="white" stroke="#1e60ff" stroke-width="2"/></svg>'
            },
            {
                'name': 'Composition',
                'description': 'A strong "has-a" relationship shown with a filled diamond, indicating that one class owns another and they have a lifecycle dependency (exclusive ownership).',
                'svg': '<svg width="200" height="50" xmlns="http://www.w3.org/2000/svg"><line x1="50" y1="25" x2="180" y2="25" stroke="#1e60ff" stroke-width="2"/><path d="M20,25 L35,15 L50,25 L35,35 Z" fill="#1e60ff" stroke="#1e60ff" stroke-width="2"/></svg>'
            },
            {
                'name': 'Inheritance',
                'description': 'An "is-a" relationship shown with a hollow triangle arrow, representing that a child class inherits from a parent class.',
                'svg': '<svg width="200" height="50" xmlns="http://www.w3.org/2000/svg"><defs><marker id="class-inherit" markerWidth="20" markerHeight="20" refX="15" refY="10" orient="auto"><path d="M0,0 L0,20 L15,10 Z" fill="white" stroke="#1e60ff" stroke-width="2"/></marker></defs><line x1="20" y1="25" x2="180" y2="25" stroke="#1e60ff" stroke-width="2" marker-end="url(#class-inherit)"/></svg>'
            },
            {
                'name': 'Multiplicity',
                'description': 'Numbers indicating how many instances of one class relate to instances of another class (e.g., 1, *, 0..1, 1..*).',
                'svg': '<svg width="200" height="60" xmlns="http://www.w3.org/2000/svg"><line x1="20" y1="30" x2="180" y2="30" stroke="#1e60ff" stroke-width="2"/><text x="10" y="20" fill="#1e60ff" font-size="12" font-weight="bold">1</text><text x="165" y="20" fill="#1e60ff" font-size="12" font-weight="bold">0..*</text><text x="80" y="50" fill="#1e60ff" font-size="11">has</text></svg>'
            }
        ],
        'example': {
            'scenario': 'Library Management System',
            'description': 'This class diagram models a library system showing relationships between Library, Book, and Member classes. The Library has a composition relationship with Books (books cannot exist without the library). Members have an aggregation relationship with Books (members can borrow books, but books exist independently). Member inherits from Person, demonstrating inheritance.',
            'svg': '<svg width="600" height="450" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ex2-comp" markerWidth="20" markerHeight="20" refX="0" refY="10" orient="auto"><path d="M0,10 L15,0 L30,10 L15,20 Z" fill="#1e60ff" stroke="#1e60ff" stroke-width="2"/></marker><marker id="ex2-agg" markerWidth="20" markerHeight="20" refX="0" refY="10" orient="auto"><path d="M0,10 L15,0 L30,10 L15,20 Z" fill="white" stroke="#1e60ff" stroke-width="2"/></marker><marker id="ex2-inherit" markerWidth="20" markerHeight="20" refX="15" refY="10" orient="auto"><path d="M0,0 L0,20 L15,10 Z" fill="white" stroke="#1e60ff" stroke-width="2"/></marker></defs><rect x="50" y="30" width="180" height="140" fill="white" stroke="#1e60ff" stroke-width="2"/><line x1="50" y1="65" x2="230" y2="65" stroke="#1e60ff" stroke-width="2"/><line x1="50" y1="110" x2="230" y2="110" stroke="#1e60ff" stroke-width="2"/><text x="140" y="52" text-anchor="middle" fill="#1e60ff" font-size="14" font-weight="bold">Library</text><text x="60" y="85" fill="#1e60ff" font-size="11">- name: String</text><text x="60" y="100" fill="#1e60ff" font-size="11">- address: String</text><text x="60" y="130" fill="#1e60ff" font-size="11">+ addBook(Book)</text><text x="60" y="145" fill="#1e60ff" font-size="11">+ removeBook(Book)</text><text x="60" y="160" fill="#1e60ff" font-size="11">+ registerMember()</text><rect x="370" y="30" width="180" height="140" fill="white" stroke="#1e60ff" stroke-width="2"/><line x1="370" y1="65" x2="550" y2="65" stroke="#1e60ff" stroke-width="2"/><line x1="370" y1="110" x2="550" y2="110" stroke="#1e60ff" stroke-width="2"/><text x="460" y="52" text-anchor="middle" fill="#1e60ff" font-size="14" font-weight="bold">Book</text><text x="380" y="85" fill="#1e60ff" font-size="11">- isbn: String</text><text x="380" y="100" fill="#1e60ff" font-size="11">- title: String</text><text x="380" y="130" fill="#1e60ff" font-size="11">+ getDetails(): String</text><text x="380" y="145" fill="#1e60ff" font-size="11">+ isAvailable(): bool</text><rect x="200" y="280" width="180" height="120" fill="white" stroke="#1e60ff" stroke-width="2"/><line x1="200" y1="315" x2="380" y2="315" stroke="#1e60ff" stroke-width="2"/><line x1="200" y1="350" x2="380" y2="350" stroke="#1e60ff" stroke-width="2"/><text x="290" y="302" text-anchor="middle" fill="#1e60ff" font-size="14" font-weight="bold">Person</text><text x="210" y="335" fill="#1e60ff" font-size="11">- name: String</text><text x="210" y="370" fill="#1e60ff" font-size="11">+ getName(): String</text><text x="210" y="385" fill="#1e60ff" font-size="11">+ setName(String)</text><rect x="420" y="280" width="180" height="130" fill="white" stroke="#1e60ff" stroke-width="2"/><line x1="420" y1="315" x2="600" y2="315" stroke="#1e60ff" stroke-width="2"/><line x1="420" y1="365" x2="600" y2="365" stroke="#1e60ff" stroke-width="2"/><text x="510" y="302" text-anchor="middle" fill="#1e60ff" font-size="14" font-weight="bold">Member</text><text x="430" y="335" fill="#1e60ff" font-size="11">- memberId: int</text><text x="430" y="350" fill="#1e60ff" font-size="11">- borrowedBooks: List</text><text x="430" y="385" fill="#1e60ff" font-size="11">+ borrowBook(Book)</text><text x="430" y="400" fill="#1e60ff" font-size="11">+ returnBook(Book)</text><line x1="230" y1="100" x2="370" y2="100" stroke="#1e60ff" stroke-width="2" marker-start="url(#ex2-comp)"/><text x="235" y="90" fill="#1e60ff" font-size="11">1</text><text x="350" y="90" fill="#1e60ff" font-size="11">*</text><text x="285" y="90" fill="#1e60ff" font-size="11">contains</text><line x1="510" y1="170" x2="510" y2="280" stroke="#1e60ff" stroke-width="2" marker-start="url(#ex2-agg)"/><text x="470" y="190" fill="#1e60ff" font-size="11">borrows</text><text x="480" y="180" fill="#1e60ff" font-size="11">*</text><text x="520" y="270" fill="#1e60ff" font-size="11">0..*</text><line x1="380" y1="340" x2="420" y2="340" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex2-inherit)"/></svg>'
        }
    },
    'activity': {
        'title': 'Activity Diagram',
        'description': {
            'what': 'An Activity Diagram is a behavioral UML diagram that represents workflows and the sequence of activities in a process. It shows the flow of control from one activity to another, including decision points, parallel processing, and synchronization. Activity diagrams are essentially enhanced flowcharts that can model complex business processes and software algorithms.',
            'why': 'Activity diagrams are crucial for modeling business processes, workflows, and use case scenarios. They help teams understand the logic flow, identify bottlenecks, and optimize processes before implementation. These diagrams are widely used in business process modeling, algorithm documentation, and system workflow analysis. They excel at showing parallel processes, decision logic, and the overall flow of activities from start to finish.'
        },
        'notations': [
            {
                'name': 'Initial Node',
                'description': 'A filled black circle representing the starting point of the workflow or process. Every activity diagram has exactly one initial node.',
                'svg': '<svg width="60" height="60" xmlns="http://www.w3.org/2000/svg"><circle cx="30" cy="30" r="15" fill="#1e60ff"/></svg>'
            },
            {
                'name': 'Final Node',
                'description': 'A circle with a filled dot inside, representing the end point of the workflow. A diagram can have multiple final nodes.',
                'svg': '<svg width="60" height="60" xmlns="http://www.w3.org/2000/svg"><circle cx="30" cy="30" r="15" fill="none" stroke="#1e60ff" stroke-width="2"/><circle cx="30" cy="30" r="9" fill="#1e60ff"/></svg>'
            },
            {
                'name': 'Action/Activity',
                'description': 'A rounded rectangle representing a single step or task in the process. Actions are atomic operations that cannot be broken down further.',
                'svg': '<svg width="160" height="60" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="140" height="40" rx="20" fill="none" stroke="#1e60ff" stroke-width="2"/><text x="80" y="35" text-anchor="middle" fill="#1e60ff" font-size="13">Process Action</text></svg>'
            },
            {
                'name': 'Decision Node',
                'description': 'A diamond shape representing a decision point where the flow branches based on conditions. Each outgoing path should be labeled with a guard condition.',
                'svg': '<svg width="80" height="80" xmlns="http://www.w3.org/2000/svg"><path d="M40,10 L70,40 L40,70 L10,40 Z" fill="none" stroke="#1e60ff" stroke-width="2"/><text x="40" y="45" text-anchor="middle" fill="#1e60ff" font-size="12">?</text></svg>'
            },
            {
                'name': 'Merge Node',
                'description': 'A diamond shape where multiple alternative flows come together. Unlike a decision, merge nodes combine paths without conditions.',
                'svg': '<svg width="80" height="80" xmlns="http://www.w3.org/2000/svg"><path d="M40,10 L70,40 L40,70 L10,40 Z" fill="none" stroke="#1e60ff" stroke-width="2"/></svg>'
            },
            {
                'name': 'Fork Node',
                'description': 'A thick horizontal or vertical bar that splits one flow into multiple parallel flows, indicating concurrent activities.',
                'svg': '<svg width="120" height="50" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="20" width="100" height="8" fill="#1e60ff"/></svg>'
            },
            {
                'name': 'Join Node',
                'description': 'A thick horizontal or vertical bar that synchronizes multiple parallel flows back into one flow, waiting for all inputs to complete.',
                'svg': '<svg width="120" height="50" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="20" width="100" height="8" fill="#1e60ff"/></svg>'
            },
            {
                'name': 'Swimlanes',
                'description': 'Vertical or horizontal partitions that organize activities by responsibility, showing which actor, department, or system performs each action.',
                'svg': '<svg width="300" height="150" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="90" height="130" fill="none" stroke="#1e60ff" stroke-width="2"/><rect x="100" y="10" width="90" height="130" fill="none" stroke="#1e60ff" stroke-width="2"/><rect x="190" y="10" width="100" height="130" fill="none" stroke="#1e60ff" stroke-width="2"/><text x="55" y="30" text-anchor="middle" fill="#1e60ff" font-size="12" font-weight="bold">Customer</text><text x="145" y="30" text-anchor="middle" fill="#1e60ff" font-size="12" font-weight="bold">System</text><text x="240" y="30" text-anchor="middle" fill="#1e60ff" font-size="12" font-weight="bold">Database</text></svg>'
            }
        ],
        'example': {
            'scenario': 'Online Order Processing',
            'description': 'This activity diagram shows the workflow of processing an online order. It starts when a customer places an order, then the system validates it. If invalid, the customer is notified; if valid, payment processing and inventory checking happen in parallel (fork). After both complete (join), the order is shipped, and the process ends.',
            'svg': '<svg width="500" height="650" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ex3-arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e60ff"/></marker></defs><circle cx="250" cy="30" r="12" fill="#1e60ff"/><line x1="250" y1="42" x2="250" y2="70" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><rect x="170" y="70" width="160" height="40" rx="20" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="250" y="95" text-anchor="middle" fill="#1e60ff" font-size="12">Receive Order</text><line x1="250" y1="110" x2="250" y2="140" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><path d="M250,140 L290,175 L250,210 L210,175 Z" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="250" y="180" text-anchor="middle" fill="#1e60ff" font-size="11">Valid?</text><line x1="210" y1="175" x2="120" y2="175" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><text x="175" y="170" text-anchor="middle" fill="#1e60ff" font-size="10">[No]</text><rect x="30" y="155" width="90" height="40" rx="20" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="75" y="180" text-anchor="middle" fill="#1e60ff" font-size="11">Notify Error</text><line x1="75" y1="195" x2="75" y2="590" stroke="#1e60ff" stroke-width="2"/><line x1="75" y1="590" x2="250" y2="590" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><line x1="250" y1="210" x2="250" y2="240" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><text x="265" y="230" fill="#1e60ff" font-size="10">[Yes]</text><rect x="200" y="240" width="100" height="8" fill="#1e60ff"/><text x="150" y="235" fill="#1e60ff" font-size="11" font-weight="bold">Fork</text><line x1="220" y1="248" x2="220" y2="280" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><line x1="280" y1="248" x2="280" y2="280" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><rect x="145" y="280" width="150" height="40" rx="20" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="220" y="305" text-anchor="middle" fill="#1e60ff" font-size="11">Process Payment</text><rect x="325" y="280" width="120" height="40" rx="20" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="385" y="305" text-anchor="middle" fill="#1e60ff" font-size="11">Check Stock</text><line x1="220" y1="320" x2="220" y2="380" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><line x1="385" y1="320" x2="385" y2="360" stroke="#1e60ff" stroke-width="2"/><line x1="385" y1="360" x2="280" y2="360" stroke="#1e60ff" stroke-width="2"/><line x1="280" y1="360" x2="280" y2="380" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><rect x="200" y="380" width="100" height="8" fill="#1e60ff"/><text x="150" y="375" fill="#1e60ff" font-size="11" font-weight="bold">Join</text><line x1="250" y1="388" x2="250" y2="420" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><rect x="170" y="420" width="160" height="40" rx="20" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="250" y="445" text-anchor="middle" fill="#1e60ff" font-size="12">Prepare Shipment</text><line x1="250" y1="460" x2="250" y2="490" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><rect x="180" y="490" width="140" height="40" rx="20" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="250" y="515" text-anchor="middle" fill="#1e60ff" font-size="12">Ship Order</text><line x1="250" y1="530" x2="250" y2="560" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex3-arrow)"/><circle cx="250" cy="590" r="15" fill="none" stroke="#1e60ff" stroke-width="2"/><circle cx="250" cy="590" r="9" fill="#1e60ff"/></svg>'
        }
    },
    'sequence': {
        'title': 'Sequence Diagram',
        'description': {
            'what': 'A Sequence Diagram is a behavioral UML diagram that shows how objects or components interact with each other over time through message exchanges. It emphasizes the time-ordered sequence of messages passed between participants. Sequence diagrams are particularly effective at showing the dynamic behavior of a system and the collaboration between different parts.',
            'why': 'Sequence diagrams are essential for understanding complex interactions in distributed systems, APIs, and multi-tier architectures. They help developers visualize the message flow, identify performance bottlenecks, and ensure proper error handling. These diagrams are extensively used in designing REST APIs, microservices communication, user authentication flows, and debugging distributed system issues. They provide a clear timeline of events, making them invaluable for both design and troubleshooting.'
        },
        'notations': [
            {
                'name': 'Lifeline',
                'description': 'A rectangle at the top with a vertical dashed line extending downward, representing an object or actor participating in the interaction over time.',
                'svg': '<svg width="120" height="150" xmlns="http://www.w3.org/2000/svg"><rect x="25" y="10" width="70" height="30" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="60" y="30" text-anchor="middle" fill="#1e60ff" font-size="12">Object</text><line x1="60" y1="40" x2="60" y2="140" stroke="#1e60ff" stroke-width="1.5" stroke-dasharray="5,5"/></svg>'
            },
            {
                'name': 'Activation Bar',
                'description': 'A thin vertical rectangle on a lifeline representing the period when an object is active or processing a message.',
                'svg': '<svg width="120" height="150" xmlns="http://www.w3.org/2000/svg"><rect x="25" y="10" width="70" height="30" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="60" y="30" text-anchor="middle" fill="#1e60ff" font-size="12">Object</text><line x1="60" y1="40" x2="60" y2="140" stroke="#1e60ff" stroke-width="1.5" stroke-dasharray="5,5"/><rect x="55" y="60" width="10" height="50" fill="#dbe8ff" stroke="#1e60ff" stroke-width="1.5"/></svg>'
            },
            {
                'name': 'Synchronous Message',
                'description': 'A solid arrow representing a message where the sender waits for a response before continuing (blocking call).',
                'svg': '<svg width="200" height="50" xmlns="http://www.w3.org/2000/svg"><defs><marker id="seq-sync" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e60ff"/></marker></defs><line x1="20" y1="25" x2="180" y2="25" stroke="#1e60ff" stroke-width="2" marker-end="url(#seq-sync)"/><text x="100" y="20" text-anchor="middle" fill="#1e60ff" font-size="11">methodCall()</text></svg>'
            },
            {
                'name': 'Return Message',
                'description': 'A dashed arrow showing the return of control or data back to the caller after processing.',
                'svg': '<svg width="200" height="50" xmlns="http://www.w3.org/2000/svg"><defs><marker id="seq-return" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e60ff"/></marker></defs><line x1="180" y1="25" x2="20" y2="25" stroke="#1e60ff" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#seq-return)"/><text x="100" y="20" text-anchor="middle" fill="#1e60ff" font-size="11">return value</text></svg>'
            },
            {
                'name': 'Asynchronous Message',
                'description': 'An open arrow representing a message where the sender does not wait for a response and continues immediately.',
                'svg': '<svg width="200" height="50" xmlns="http://www.w3.org/2000/svg"><defs><marker id="seq-async" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="none" stroke="#1e60ff" stroke-width="2"/></marker></defs><line x1="20" y1="25" x2="180" y2="25" stroke="#1e60ff" stroke-width="2" marker-end="url(#seq-async)"/><text x="100" y="20" text-anchor="middle" fill="#1e60ff" font-size="11">asyncCall()</text></svg>'
            },
            {
                'name': 'Destroy/Delete',
                'description': 'An "X" symbol at the end of a lifeline indicating that the object is destroyed or goes out of scope.',
                'svg': '<svg width="100" height="140" xmlns="http://www.w3.org/2000/svg"><rect x="15" y="10" width="70" height="30" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="50" y="30" text-anchor="middle" fill="#1e60ff" font-size="12">Object</text><line x1="50" y1="40" x2="50" y2="100" stroke="#1e60ff" stroke-width="1.5" stroke-dasharray="5,5"/><line x1="40" y1="100" x2="60" y2="120" stroke="#1e60ff" stroke-width="3"/><line x1="60" y1="100" x2="40" y2="120" stroke="#1e60ff" stroke-width="3"/></svg>'
            },
            {
                'name': 'Interaction Frame',
                'description': 'A rectangle with a label (alt, loop, opt, par) in the corner, used to show conditional logic, loops, or parallel processing.',
                'svg': '<svg width="280" height="140" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="260" height="120" fill="none" stroke="#1e60ff" stroke-width="2"/><rect x="10" y="10" width="50" height="25" fill="#1e60ff"/><text x="35" y="27" text-anchor="middle" fill="white" font-size="12" font-weight="bold">alt</text><line x1="10" y1="75" x2="270" y2="75" stroke="#1e60ff" stroke-width="1.5" stroke-dasharray="5,5"/><text x="20" y="50" fill="#1e60ff" font-size="11">[condition1]</text><text x="20" y="95" fill="#1e60ff" font-size="11">[else]</text></svg>'
            }
        ],
        'example': {
            'scenario': 'User Login Authentication',
            'description': 'This sequence diagram illustrates a typical user login process. The User interacts with the LoginPage, which sends credentials to the AuthService. The AuthService validates credentials against the Database. If valid, a session token is created and returned; if invalid, an error message is displayed. This shows synchronous calls, return messages, and the interaction flow between frontend, backend, and database.',
            'svg': '<svg width="650" height="500" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ex4-arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e60ff"/></marker></defs><rect x="40" y="20" width="80" height="35" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="80" y="42" text-anchor="middle" fill="#1e60ff" font-size="12" font-weight="bold">User</text><line x1="80" y1="55" x2="80" y2="480" stroke="#1e60ff" stroke-width="1.5" stroke-dasharray="5,5"/><rect x="185" y="20" width="110" height="35" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="240" y="42" text-anchor="middle" fill="#1e60ff" font-size="12" font-weight="bold">LoginPage</text><line x1="240" y1="55" x2="240" y2="480" stroke="#1e60ff" stroke-width="1.5" stroke-dasharray="5,5"/><rect x="360" y="20" width="120" height="35" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="420" y="42" text-anchor="middle" fill="#1e60ff" font-size="12" font-weight="bold">AuthService</text><line x1="420" y1="55" x2="420" y2="480" stroke="#1e60ff" stroke-width="1.5" stroke-dasharray="5,5"/><rect x="540" y="20" width="90" height="35" fill="white" stroke="#1e60ff" stroke-width="2"/><text x="585" y="42" text-anchor="middle" fill="#1e60ff" font-size="12" font-weight="bold">Database</text><line x1="585" y1="55" x2="585" y2="480" stroke="#1e60ff" stroke-width="1.5" stroke-dasharray="5,5"/><line x1="80" y1="85" x2="240" y2="85" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex4-arrow)"/><text x="160" y="80" text-anchor="middle" fill="#1e60ff" font-size="10">enterCredentials()</text><rect x="235" y="90" width="10" height="290" fill="#dbe8ff" stroke="#1e60ff" stroke-width="1.5"/><line x1="240" y1="115" x2="420" y2="115" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex4-arrow)"/><text x="330" y="110" text-anchor="middle" fill="#1e60ff" font-size="10">login(user, pass)</text><rect x="415" y="120" width="10" height="230" fill="#dbe8ff" stroke="#1e60ff" stroke-width="1.5"/><line x1="420" y1="145" x2="585" y2="145" stroke="#1e60ff" stroke-width="2" marker-end="url(#ex4-arrow)"/><text x="502" y="140" text-anchor="middle" fill="#1e60ff" font-size="10">validateUser()</text><rect x="580" y="150" width="10" height="60" fill="#dbe8ff" stroke="#1e60ff" stroke-width="1.5"/><line x1="585" y1="185" x2="420" y2="185" stroke="#1e60ff" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#ex4-arrow)"/><text x="502" y="180" text-anchor="middle" fill="#1e60ff" font-size="10">userRecord</text><rect x="20" y="220" width="610" height="110" fill="none" stroke="#1e60ff" stroke-width="2"/><rect x="20" y="220" width="45" height="22" fill="#1e60ff"/><text x="42" y="235" text-anchor="middle" fill="white" font-size="11" font-weight="bold">alt</text><text x="30" y="255" fill="#1e60ff" font-size="10">[valid]</text><line x1="20" y1="285" x2="630" y2="285" stroke="#1e60ff" stroke-width="1.5" stroke-dasharray="5,5"/><text x="30" y="305" fill="#1e60ff" font-size="10">[invalid]</text><line x1="420" y1="265" x2="240" y2="265" stroke="#1e60ff" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#ex4-arrow)"/><text x="330" y="260" text-anchor="middle" fill="#1e60ff" font-size="10">sessionToken</text><line x1="420" y1="315" x2="240" y2="315" stroke="#1e60ff" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#ex4-arrow)"/><text x="330" y="310" text-anchor="middle" fill="#1e60ff" font-size="10">error</text><line x1="240" y1="355" x2="80" y2="355" stroke="#1e60ff" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#ex4-arrow)"/><text x="160" y="350" text-anchor="middle" fill="#1e60ff" font-size="10">showDashboard()</text><line x1="240" y1="395" x2="80" y2="395" stroke="#1e60ff" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#ex4-arrow)"/><text x="160" y="390" text-anchor="middle" fill="#1e60ff" font-size="10">showError()</text></svg>'
        }
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagram/<diagram_name>')
def diagram(diagram_name):
    diagram_data = UML_CONTENT.get(diagram_name)
    if not diagram_data:
        return redirect(url_for('index'))
    return render_template('diagram.html', diagram=diagram_data, diagram_name=diagram_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
