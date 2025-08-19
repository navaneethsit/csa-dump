questions = [
    {
        "question": "A Service Catalog may include which of the following components?",
        "options": [
            "A. Order Guides, Exchange Rates, Calendars",
            "B. Order Guides, Catalog Items, and Interceptors",
            "C. Catalog Items, Asset Contracts, Task Surveys",
            "D. Record Producers, Order Guides, and Catalog Item"
        ],
        "answer": "B. Order Guides, Catalog Items, and Interceptors",
        "explanation": "A Service Catalog includes Order Guides to bundle items, Catalog Items for individual services or products, and Interceptors to guide users to the appropriate catalog item."
    },
    {
        "question": "Which one of the following statements applies to a set of fields when they are coalesced during an import?",
        "options": [
            "A. If a match is found using the coalesce fields, the existing record is updated with the information being imported",
            "B. If a match is not found using the coalesce fields, the system does not create a Transform Map",
            "C. If a match is found using the coalesce fields, the system creates a new record",
            "D. If a match is not found using the coalesce fields, the existing record is updated with the information being imported"
        ],
        "answer": "A. If a match is found using the coalesce fields, the existing record is updated with the information being imported",
        "explanation": "Coalesce fields act as unique identifiers during imports. If a match is found, the existing record is updated; if no match is found, a new record is created."
    },
    {
        "question": "As it relates to ServiceNow reporting, which of the following statements describes what a metric can do?",
        "options": [
            "A. A metric is a report gauge used on homepages to display real-time data",
            "B. A metric is a time measurement used to report the effectiveness of workflows and SLAs",
            "C. A metric is used to measure and evaluate the effectiveness of IT service management processes",
            "D. A metric is a comparative measurement used to report the effectiveness of flows and SLAs"
        ],
        "answer": "C. A metric is used to measure and evaluate the effectiveness of IT service management processes",
        "explanation": "Metrics in ServiceNow track and evaluate the performance of IT service management processes, such as incident or problem management."
    },
    {
        "question": "The display sequence is controlled in a Service Catalog Item using which of the following?",
        "options": [
            "A. The Default Value field in the Catalog Item form",
            "B. The Sequence field in the Catalog Item form",
            "C. The Order field in the Variable form",
            "D. The Choice field in the Variable form"
        ],
        "answer": "C. The Order field in the Variable form",
        "explanation": "The Order field in the Variable form determines the display sequence of variables in a Service Catalog Item."
    },
    {
        "question": "Reports can be created from which different places in the platform? (Choose two.)",
        "options": [
            "A. List column heading",
            "B. Metrics module",
            "C. Statistics module",
            "D. View / Run module"
        ],
        "answer": "A. List column heading, D. View / Run module",
        "explanation": "Reports can be created by right-clicking a column heading in a list or through the View / Run module in the Reports application."
    },
    {
        "question": "Knowledge Base Search results can be sorted by which of the following? (Choose three.)",
        "options": [
            "A. Most recent update",
            "B. Popularity",
            "C. Relevancy",
            "D. Manager assignment",
            "E. Number of views"
        ],
        "answer": "A. Most recent update, C. Relevancy, E. Number of views",
        "explanation": "Knowledge Base search results can be sorted by most recent update, relevancy, and number of views to help users find relevant articles."
    },
    {
        "question": "What is the path an Administrator could take to view the fulfillment stage task list for an order placed by a user?",
        "options": [
            "A. RITM (Number)>REQ (Number)>PROCUREMENT (Number)",
            "B. REQ (Number)>RITM (Number)>PROCUREMENT (Number)",
            "C. REQ (Number)>RITM (Number)>TASK (Number)",
            "D. FULFILLMENT (Number)>RITM (Number)>TASK (Number)"
        ],
        "answer": "C. REQ (Number)>RITM (Number)>TASK (Number)",
        "explanation": "To view the fulfillment stage task list, navigate from the Request (REQ) to the Requested Item (RITM) to the associated Task (TASK)."
    },
    {
        "question": "Which term refers to application menus and modules which you may want to access quickly and often?",
        "options": [
            "A. Breadcrumb",
            "B. Favorite",
            "C. Tag",
            "D. Bookmark"
        ],
        "answer": "B. Favorite",
        "explanation": "Favorites in ServiceNow allow users to quickly access frequently used application menus and modules."
    },
    {
        "question": "What is generated from the Service Catalog once a user places an order for an item or service?",
        "options": [
            "A. A change request",
            "B. An Order Guide",
            "C. A request",
            "D. An SLA"
        ],
        "answer": "C. A request",
        "explanation": "When a user places an order in the Service Catalog, a Request (REQ) record is generated."
    },
    {
        "question": "From the User menu, which actions can a user select? (Choose three.)",
        "options": [
            "A. Send Notifications",
            "B. Log Out ServiceNow",
            "C. Elevate Roles",
            "D. Impersonate Users",
            "E. Order from Service Catalog",
            "F. Approve Records"
        ],
        "answer": "B. Log Out ServiceNow, C. Elevate Roles, D. Impersonate Users",
        "explanation": "From the User menu, users can log out, elevate roles (if permitted), or impersonate other users (with appropriate permissions)."
    },
    {
        "question": "Buttons, form links, and context menu items are all examples of what type of functionality?",
        "options": [
            "A. Business Rule",
            "B. UI Action",
            "C. Client Script",
            "D. UI Policy"
        ],
        "answer": "B. UI Action",
        "explanation": "UI Actions are used to create buttons, form links, and context menu items that trigger specific functionalities."
    },
    {
        "question": "Which of the following is true of Service Catalog Items in relation to the Service Catalog?",
        "options": [
            "A. They run behind the scenes.",
            "B. They are the building blocks.",
            "C. They are optional.",
            "D. They provide options."
        ],
        "answer": "B. They are the building blocks.",
        "explanation": "Service Catalog Items are the core components of the Service Catalog, defining services or products users can request."
    },
    {
        "question": "Table Access Control rules are processed in the following order:",
        "options": [
            "A. any table name (wildcard), parent table name, table name",
            "B. table name, parent table name, any table name (wildcard)",
            "C. parent table name, table name, any table name (wildcard)",
            "D. any table name (wildcard), table name, parent table name"
        ],
        "answer": "B. table name, parent table name, any table name (wildcard)",
        "explanation": "Access Control rules are evaluated in this order to determine permissions, starting with the specific table, then parent, then wildcard."
    },
    {
        "question": "What is the platform name for the User table?",
        "options": [
            "A. u_users",
            "B. sys_users",
            "C. x_users",
            "D. sys_user"
        ],
        "answer": "D. sys_user",
        "explanation": "The platform name for the User table in ServiceNow is sys_user."
    },
    {
        "question": "A REQ number in the Service Catalog represents...",
        "options": [
            "A. the order number.",
            "B. the stage.",
            "C. the task to complete.",
            "D. the individual item in the order."
        ],
        "answer": "A. the order number.",
        "explanation": "A REQ number represents the overall order (Request) in the Service Catalog."
    },
    {
        "question": "Which would NOT appear in the History section of the Application Navigator?",
        "options": [
            "A. Records",
            "B. UI Pages",
            "C. Lists",
            "D. Forms"
        ],
        "answer": "B. UI Pages",
        "explanation": "UI Pages would NOT appear in the History section of the Application Navigator. The History section shows recently accessed Records, Lists, and Forms, but UI Pages are not tracked in the navigation history."
    },
    {
        "question": "Which one of the following statements is a recommendation from ServiceNow about Update Sets?",
        "options": [
            "A. Avoid using the Default Update set as an Update Set for moving customizations from instance to instance",
            "B. Before moving customizations from instance to instance with Update Sets, ensure that both instances are different versions",
            "C. Use the Baseline Update Set to store the contents of items after they are changed the first time",
            "D. Once an Update Set is closed as 'Complete', change it back to 'In Progress' until it is applied to another instance"
        ],
        "answer": "A. Avoid using the Default Update set as an Update Set for moving customizations from instance to instance",
        "explanation": "ServiceNow recommends using named Update Sets for better tracking and management of customizations, avoiding the Default Update Set."
    },
    {
        "question": "Which of the following is used to initiate a flow?",
        "options": [
            "A. A Trigger",
            "B. Core Action",
            "C. A spoke",
            "D. An Event"
        ],
        "answer": "A. A Trigger",
        "explanation": "A flow in Flow Designer is initiated by a trigger, which defines when the flow should run."
    },
    {
        "question": "For Administrators creating new Service Catalog items, what is a characteristic they should know about Service Catalog variables?",
        "options": [
            "A. Service Catalog variables can only be used in Record Producers",
            "B. Service Catalog variables can only be used in Order Guides",
            "C. Service Catalog variables cannot affect the order price",
            "D. Service Catalog variables are global by default"
        ],
        "answer": "D. Service Catalog variables are global by default",
        "explanation": "Service Catalog variables are global by default unless explicitly scoped to a specific catalog item or order guide."
    },
    {
        "question": "Which one of the following statements is true about Column Context Menus?",
        "options": [
            "A. It displays actions such as creating quick reports, configuring the list, and exporting data",
            "B. It displays actions related to filtering options, assigning tags, and search",
            "C. It displays actions related to viewing and filtering the entire list",
            "D. It displays actions such as view form, view related task, and add relationship"
        ],
        "answer": "A. It displays actions such as creating quick reports, configuring the list, and exporting data",
        "explanation": "Column Context Menus provide options like creating reports, configuring lists, and exporting data from a list view."
    },
    {
        "question": "Which ServiceNow products can be used to discover and populate the CMDB? (Choose two.)",
        "options": [
            "A. Discovery",
            "B. IntegrationHub ETL",
            "C. Finder",
            "D. CMDB Plug-in",
            "E. CMDB Integration Dashboard"
        ],
        "answer": "A. Discovery, B. IntegrationHub ETL",
        "explanation": "Discovery and IntegrationHub ETL are used to discover and populate the CMDB with configuration item data."
    },
    {
        "question": "When using the Load Data and Transform Map process, what is the Mapping Assist used for?",
        "options": [
            "A. Mapping fields using the Import Log",
            "B. Mapping fields using Transform History",
            "C. Mapping fields using an SLA",
            "D. Mapping fields using a Field Map"
        ],
        "answer": "D. Mapping fields using a Field Map",
        "explanation": "Mapping Assist is used to map fields between an import set table and a target table during data import."
    },
    {
        "question": "Which one of the following statements describes the contents of the Configuration Management Database (CMDB)?",
        "options": [
            "A. The CMDB contains data about tangible and intangible business assets",
            "B. The CMDB contains the Business Rules that direct the intangible, configurable assets used by a company",
            "C. The CMDB archives all Service Management PaaS equipment metadata and usage statistics",
            "D. The CMDB contains ITIL process data pertaining to configuration items"
        ],
        "answer": "A. The CMDB contains data about tangible and intangible business assets",
        "explanation": "The CMDB stores information about configuration items, including tangible assets (e.g., servers) and intangible assets (e.g., services)."
    },
    {
        "question": "In what order should filter elements be specified?",
        "options": [
            "A. Field, Operator, then Value",
            "B. Field, Operator, then Condition",
            "C. Operator, Condition, then Value",
            "D. Value, Operator, then Field"
        ],
        "answer": "A. Field, Operator, then Value",
        "explanation": "Filter elements in ServiceNow are specified as Field, Operator, and Value to create conditions for data retrieval."
    },
    {
        "question": "Which statement is true about business rules?",
        "options": [
            "A. A business rule must run before a database action occurs",
            "B. A business rule can be a piece of Javascript",
            "C. A business rule must not run before a database action occurs",
            "D. A business rule monitors fields on a form"
        ],
        "answer": "B. A business rule can be a piece of Javascript",
        "explanation": "Business Rules are server-side scripts written in JavaScript to enforce business logic."
    },
    {
        "question": "Which of the following are a type of client scripts supported in ServiceNow? (Choose four.)",
        "options": [
            "A. onSubmit",
            "B. onUpdate",
            "C. onCellEdit",
            "D. onLoad",
            "E. onEdit",
            "F. onChange",
            "G. onSave"
        ],
        "answer": "A. onSubmit, C. onCellEdit, D. onLoad, F. onChange",
        "explanation": "ServiceNow supports onSubmit, onCellEdit, onLoad, and onChange as client script types for form interactions."
    },
    {
        "question": "Which type of tables may be extended by other tables, but do not extend another table?",
        "options": [
            "A. Base Tables",
            "B. Core Tables",
            "C. Extended Tables",
            "D. Custom Tables"
        ],
        "answer": "A. Base Tables",
        "explanation": "Base tables do not extend other tables but can be extended by other tables."
    },
    {
        "question": "Which of the following statement describes the purpose of an Order Guide?",
        "options": [
            "A. Order Guides restrict the number of items in an order to only one item per request",
            "B. Order Guide provide a list of guidelines for Administrators on how to set up item variables",
            "C. Order Guide provide the ability to order multiple, related items as one request",
            "D. Order Guides take the user directly to the checkout without prompting for information"
        ],
        "answer": "C. Order Guide provide the ability to order multiple, related items as one request",
        "explanation": "Order Guides bundle related catalog items into a single request for streamlined ordering."
    },
    {
        "question": "Which tool is used to have conversations with logged-in users in real-time?",
        "options": [
            "A. Connect Chat",
            "B. Now Messenger",
            "C. User Presence",
            "D. Comments"
        ],
        "answer": "A. Connect Chat",
        "explanation": "Connect Chat is used for real-time conversations with logged-in users in ServiceNow."
    },
    {
        "question": "Which of the following concepts are associated with the ServiceNow CMDB? (Choose four.)",
        "options": [
            "A. Service Processes",
            "B. User Permissions",
            "C. Tables and Fields",
            "D. A Database",
            "E. The Dependency View",
            "F. CI Relationships"
        ],
        "answer": "C. Tables and Fields, D. A Database, E. The Dependency View, F. CI Relationships",
        "explanation": "The CMDB involves tables and fields, is a database, includes Dependency Views for relationships, and manages CI relationships."
    },
    {
        "question": "What is a formatter?",
        "options": [
            "A. A formatter allows you to configure applications on your instance",
            "B. A formatter is a form element used to display information that is not a field in the record",
            "C. A formatter allows you to populate fields automatically",
            "D. A formatter is a set of conditions applied to a table to help find and work with data"
        ],
        "answer": "B. A formatter is a form element used to display information that is not a field in the record",
        "explanation": "Formatters, like the Activity Stream, display additional information on a form that isn’t stored in a field."
    },
    {
        "question": "When searching using the App Navigator search field, what can be returned? (Choose four.)",
        "options": [
            "A. Names of Applications and Modules",
            "B. Names of Modules",
            "C. Names of Applications",
            "D. Favorites",
            "E. History Records",
            "F. Titles of Dashboard Gauges"
        ],
        "answer": "A. Names of Applications and Modules, B. Names of Modules, C. Names of Applications, D. Favorites",
        "explanation": "The Application Navigator search returns Applications, Modules, and Favorites for quick access."
    },
    {
        "question": "Which technique is used to get information from a series of referenced fields from different tables?",
        "options": [
            "A. Table-Walking",
            "B. Sys_ID Pulling",
            "C. Dot-Walking",
            "D. Record-Hopping"
        ],
        "answer": "C. Dot-Walking",
        "explanation": "Dot-Walking allows access to fields from related tables via reference fields."
    },
    {
        "question": "What is a schema map?",
        "options": [
            "A. A schema map enables administrators to define records from specific tables as trouble sources for Configuration Items",
            "B. A schema map graphically organizes the visual task boards for the CMDB",
            "C. A schema map graphically displays the Configuration Items that support a business service",
            "D. A schema map displays the details of tables and their relationships in a visual manner, allowing administrators to view and easily access different parts of the database schema"
        ],
        "answer": "D. A schema map displays the details of tables and their relationships in a visual manner, allowing administrators to view and easily access different parts of the database schema",
        "explanation": "Schema maps provide a visual representation of table relationships in ServiceNow."
    },
    {
        "question": "Which one of the following statements best describes the purpose of an Update Set?",
        "options": [
            "A. An Update Set allows administrators to group a series of changes into a named set and then move this set as a unit to other systems",
            "B. By default, an Update Set includes customizations, Business Rules, and homepages",
            "C. An Update Set is a group of customizations that is moved from Production to Development",
            "D. By default, the changes included in an Update Set are visible only in the instance to which they are applied"
        ],
        "answer": "A. An Update Set allows administrators to group a series of changes into a named set and then move this set as a unit to other systems",
        "explanation": "Update Sets package and transfer customizations between ServiceNow instances."
    },
    {
        "question": "Which of the following can be customized through the Basic Configuration UI 16 module? (Choose three.)",
        "options": [
            "A. Banner Image",
            "B. Record Number Format",
            "C. Browser Tab Title",
            "D. System Date Format",
            "E. Form Header Size"
        ],
        "answer": "A. Banner Image, C. Browser Tab Title, D. System Date Format",
        "explanation": "The Basic Configuration UI16 module allows customization of the banner image, browser tab title, and system date format."
    },
    {
        "question": "What is the function of user impersonation?",
        "options": [
            "A. Testing and visibility",
            "B. Activate verbose logging",
            "C. View custom perspectives",
            "D. Unlock Application master list"
        ],
        "answer": "A. Testing and visibility",
        "explanation": "User impersonation is used to test how the system appears to other users and verify visibility."
    },
    {
        "question": "What information does the System Dictionary contain?",
        "options": [
            "A. The human-readable labels and language settings",
            "B. The definition for each table and column",
            "C. The information on how tables relate to each other",
            "D. The language dictionary used for spell checking"
        ],
        "answer": "B. The definition for each table and column",
        "explanation": "The System Dictionary contains metadata about tables and fields in ServiceNow."
    },
    {
        "question": "When working on a form, what is the difference between Insert and Update operations?",
        "options": [
            "A. Insert creates a new record and Update saves changes, both remain on the form",
            "B. Insert creates a new record and Update saves changes, both exit the form",
            "C. Insert saves changes and exits the form, Update saves changes and remains on the form",
            "D. Insert saves changes and remains on the form, Update saves changes and exits the form"
        ],
        "answer": "A. Insert creates a new record and Update saves changes, both remain on the form",
        "explanation": "Insert creates a new record, and Update saves changes to an existing record, both keeping the user on the form."
    },
    {
        "question": "How is the Event Log different from the Event Registry?",
        "options": [
            "A. Event Log contains generated Events, the Event Registry is a table of Event definitions",
            "B. Event Log is formatted in the Log style, the Event Registry displays different fields",
            "C. Event Log lists Events that were triggered by integrations, the Event Registry lists the Events that were triggered during the day (24-hour period)",
            "D. Event Log is the same as the Event Registry"
        ],
        "answer": "A. Event Log contains generated Events, the Event Registry is a table of Event definitions",
        "explanation": "The Event Log records triggered events, while the Event Registry defines event types."
    },
    {
        "question": "What is a Dictionary Override?",
        "options": [
            "A. A Dictionary Override is an incoming customer update in an Update Set which applies to the same objects as a newer local customer update",
            "B. A Dictionary Override is the addition, modification, or removal of anything that could have an effect on IT services",
            "C. A Dictionary Override is a task within a flow that requests an action before the flow can continue",
            "D. A Dictionary Override sets field properties in extended tables"
        ],
        "answer": "D. A Dictionary Override sets field properties in extended tables",
        "explanation": "Dictionary Overrides allow customization of field properties in extended tables."
    },
    {
        "question": "Which group of permissions is used to control Application and Module access?",
        "options": [
            "A. Access Control Rules",
            "B. UI Policies",
            "C. Roles",
            "D. Assignment Rules"
        ],
        "answer": "C. Roles",
        "explanation": "Roles control access to applications and modules in ServiceNow."
    },
    {
        "question": "What is a Record Producer?",
        "options": [
            "A. A Record Producer is a type of Catalog Item that is used for Requests, not Services",
            "B. A Record Producer creates user records",
            "C. A Record Producer is a type of Catalog Item that provides easy ordering by bundling requests",
            "D. A Record Producer is a type of a Catalog Item that allows users to create task-based records from the Service Catalog"
        ],
        "answer": "D. A Record Producer is a type of a Catalog Item that allows users to create task-based records from the Service Catalog",
        "explanation": "Record Producers simplify task creation from the Service Catalog."
    },
    {
        "question": "Create Incident, Password Reset, and Report outage: what do these services in the Service Catalog have in common?",
        "options": [
            "A. They direct the user to a record producer",
            "B. They direct the user to a catalog property",
            "C. They direct the user to a catalog UI policy",
            "D. They direct the user to a catalog client script"
        ],
        "answer": "A. They direct the user to a record producer",
        "explanation": "These services typically use Record Producers to create task-based records."
    },
    {
        "question": "What is the Import Set Table?",
        "options": [
            "A. A table where data will be placed, post-transformation",
            "B. A table that determines relationships",
            "C. A staging area for imported records",
            "D. A repository for Update Set information"
        ],
        "answer": "C. A staging area for imported records",
        "explanation": "The Import Set Table temporarily holds data during the import process before transformation."
    },
    {
        "question": "What is a characteristic of importing data into ServiceNow?",
        "options": [
            "A. An existing Transform Map can be used one time on the same import set",
            "B. Coalesce fields are used only after running Transform",
            "C. Any user can manage and set up import sets",
            "D. An existing Transform Map can be used multiple times on the same import set"
        ],
        "answer": "D. An existing Transform Map can be used multiple times on the same import set",
        "explanation": "Transform Maps can be reused for multiple imports to map data to target tables."
    },
    {
        "question": "What module in the Service Catalog application does an Administrator access to begin creating a new item?",
        "options": [
            "A. Maintain Categories",
            "B. Maintain Items",
            "C. Content Items",
            "D. Items"
        ],
        "answer": "B. Maintain Items",
        "explanation": "Administrators use the Maintain Items module to create new Service Catalog items."
    },
    {
        "question": "Which of the following allows a user to edit field values in a list without opening the form?",
        "options": [
            "A. Data Editor",
            "B. Edit Menu",
            "C. List Editor",
            "D. Form Designer"
        ],
        "answer": "C. List Editor",
        "explanation": "The List Editor allows users to edit field values directly in a list without opening the form."
    },
    {
        "question": "Which three Variable Types can be added to a Service Catalog Item?",
        "options": [
            "A. True/False, Multiple Choice, and Ordered",
            "B. True/False, Checkbox, and Number List",
            "C. Number List, Single Line Text, and Reference",
            "D. Multiple Choice, Select Box, and Checkbox"
        ],
        "answer": "D. Multiple Choice, Select Box, and Checkbox",
        "explanation": "These are valid variable types for Service Catalog Items."
    },
    {
        "question": "How are Workflows moved between instances?",
        "options": [
            "A. Workflows are moved using Update Sets",
            "B. Workflows are moved using Transform Maps",
            "C. Workflows are moved using Application Sets",
            "D. Workflows cannot be moved between instances"
        ],
        "answer": "A. Workflows are moved using Update Sets",
        "explanation": "Workflows are included in Update Sets for transfer between instances."
    },
    {
        "question": "The baseline Service Catalog homepage contains links to which of the following components?",
        "options": [
            "A. Record Producers, Order Guides, and Catalog Items",
            "B. Order Guides, Item Variables, and flows",
            "C. Order Guides, Catalog Items, and flows",
            "D. Record Producers, Order Guides, and Item Variables"
        ],
        "answer": "A. Record Producers, Order Guides, and Catalog Items",
        "explanation": "The Service Catalog homepage includes links to Record Producers, Order Guides, and Catalog Items."
    },
    {
        "question": "Which of the following statements is true when a new table is created by extending another table?",
        "options": [
            "A. The new table archives the parent table and assumed its roles in the database",
            "B. The new table inherits all of the Business Rules, Client Scripts, and UI Policies of the parent table, but none of the existing fields",
            "C. The new table inherits all of the fields of the parent table and can also contain new fields unique to itself",
            "D. The new table inherits all of the fields, but does not inherit Access Control rules, Client Scripts, and UI Policies of the parent table"
        ],
        "answer": "C. The new table inherits all of the fields of the parent table and can also contain new fields unique to itself",
        "explanation": "Extended tables inherit fields from their parent and can add unique fields."
    },
    {
        "question": "Where can Admins check which release is running on a ServiceNow instance?",
        "options": [
            "A. Memory Stats module",
            "B. Stats module",
            "C. System.upgraded table",
            "D. Transactions log"
        ],
        "answer": "B. Stats module",
        "explanation": "The Stats module displays the current release version of a ServiceNow instance."
    },
    {
        "question": "A knowledge article must be which of the following states to display to a user?",
        "options": [
            "A. Published",
            "B. Drafted",
            "C. Retired",
            "D. Reviewed"
        ],
        "answer": "A. Published",
        "explanation": "Knowledge articles must be in the Published state to be visible to users."
    },
    {
        "question": "What is the name of the conversational bot platform that provides assistance to help users obtain information, make decisions, and perform common tasks?",
        "options": [
            "A. Answer Agent",
            "B. Live Feed",
            "C. Virtual Agent",
            "D. Connect Chat"
        ],
        "answer": "C. Virtual Agent",
        "explanation": "The Virtual Agent is ServiceNow’s conversational bot platform for assisting users."
    },
    {
        "question": "What is the purpose of a Related List?",
        "options": [
            "A. To create a one-to-many relationship",
            "B. To dot-walk to a core table",
            "C. To present related fields",
            "D. To present related records"
        ],
        "answer": "D. To present related records",
        "explanation": "Related Lists display records related to the current record on a form."
    },
    {
        "question": "Which one of the following statements describes the purpose of a Service Catalog flow?",
        "options": [
            "A. A Service Catalog flow generates three basic components: item variable types, tasks, and approvals",
            "B. Although a Service Catalog flow cannot send notifications, the flow drives complex fulfillment processes",
            "C. A Service Catalog flow is used to drive complex fulfillment processes and sends notifications to defined users or groups",
            "D. A Service Catalog flow generates three basic components: item variable types, tasks, and notifications"
        ],
        "answer": "C. A Service Catalog flow is used to drive complex fulfillment processes and sends notifications to defined users or groups",
        "explanation": "Service Catalog flows manage fulfillment processes and send notifications to users or groups."
    },
    {
        "question": "Which term best describes something that is created, has worked performed upon it, and is eventually moved to a state of closed?",
        "options": [
            "A. Report",
            "B. Flow",
            "C. Event",
            "D. Task"
        ],
        "answer": "D. Task",
        "explanation": "Tasks are created, worked on, and eventually closed in ServiceNow."
    },
    {
        "question": "Which are valid ServiceNow User Authentication Methods? (Choose three.)",
        "options": [
            "A. XML feed",
            "B. Local database",
            "C. LDAP",
            "D. SSO",
            "E. FTP authentication"
        ],
        "answer": "B. Local database, C. LDAP, D. SSO",
        "explanation": "ServiceNow supports local database, LDAP, and SSO as user authentication methods."
    },
    {
        "question": "Access Control rules may be defined with which of the following permission requirements? (Choose three.)",
        "options": [
            "A. Roles",
            "B. Conditional Expressions",
            "C. Assignment Rules",
            "D. Scripts",
            "E. User Criteria",
            "F. Groups"
        ],
        "answer": "A. Roles, B. Conditional Expressions, D. Scripts",
        "explanation": "Access Control rules can use Roles, Conditional Expressions, and Scripts to define permissions."
    },
    {
        "question": "Which section of the ServiceNow UI allows you to perform a global search?",
        "options": [
            "A. Application Navigator",
            "B. Banner frame",
            "C. List pane",
            "D. Content frame"
        ],
        "answer": "A. Application Navigator",
        "explanation": "The Application Navigator includes a global search field for searching across the platform."
    },
    {
        "question": "How do you make a list filter available to everyone?",
        "options": [
            "A. Make active, assign a name, and save",
            "B. Assign a group, set visibility, and save",
            "C. Assign a name, set visibility, and save",
            "D. Make active, set visibility, and save"
        ],
        "answer": "D. Make active, set visibility, and save",
        "explanation": "To share a list filter, make it active, set visibility to public, and save it."
    },
    {
        "question": "What would NOT appear in the Application Navigator if 'service' is typed into the filter field?",
        "options": [
            "A. Configuration > Business Services",
            "B. Self-Service > Knowledge",
            "C. Service Portal > Widgets",
            "D. Incident > Assigned to me"
        ],
        "answer": "C. Service Portal > Widgets",
        "explanation": "Typing 'service' in the Application Navigator filter won’t return Service Portal > Widgets, as it’s not directly related to the term 'service.'"
    },
    {
        "question": "Which of the following is used to categorize, flag, and locate records?",
        "options": [
            "A. Search",
            "B. Favorites",
            "C. Tags",
            "D. Bookmarks"
        ],
        "answer": "C. Tags",
        "explanation": "Tags are used to categorize, flag, and locate records in ServiceNow."
    },
    {
        "question": "Which tool should be used to populate commonly used fields in a form?",
        "options": [
            "A. Template",
            "B. Reference Qualifier",
            "C. Formatter",
            "D. Assignment Rule"
        ],
        "answer": "A. Template",
        "explanation": "Templates are used to populate commonly used fields in a form."
    },
    {
        "question": "How is a group defined in ServiceNow?",
        "options": [
            "A. A group is one record stored in the Group Type [sys_user_group_type] table",
            "B. A group is one record stored in the Group [sys_user_group] table",
            "C. A group defines a set of users that share the same location",
            "D. A group defines a set of users that share the same job title"
        ],
        "answer": "B. A group is one record stored in the Group [sys_user_group] table",
        "explanation": "Groups are stored as records in the sys_user_group table."
    },
    {
        "question": "What is a role in ServiceNow?",
        "options": [
            "A. A role is one record in the Role [user_sys_role] table",
            "B. A role is a set of modules for a particular application",
            "C. A role is one record in the Role [sys_user_role] table",
            "D. A role is a persona used in Live Feed Chat"
        ],
        "answer": "C. A role is one record in the Role [sys_user_role] table",
        "explanation": "Roles are defined as records in the sys_user_role table."
    },
    {
        "question": "What is a Notification?",
        "options": [
            "A. A new Knowledge article created by a Business Rule",
            "B. A tool for alerting users that events that concern them have occurred",
            "C. A message through Connect related to a Change Request",
            "D. An email file attachment"
        ],
        "answer": "B. A tool for alerting users that events that concern them have occurred",
        "explanation": "Notifications alert users about relevant events or updates in ServiceNow."
    },
    {
        "question": "Which one of the following is NOT a type of Visual Task Board?",
        "options": [
            "A. Flexible",
            "B. Freeform",
            "C. Feature",
            "D. Guided boards"
        ],
        "answer": "C. Feature",
        "explanation": "Feature is not a type of Visual Task Board; Flexible, Freeform, and Guided boards are valid types."
    },
    {
        "question": "What are best practice(s) regarding users/groups/roles? (Choose two.)",
        "options": [
            "A. You should never assign roles to groups.",
            "B. You should assign roles to users.",
            "C. You should add users to groups.",
            "D. You should assign roles to groups."
        ],
        "answer": "C. You should add users to groups., D. You should assign roles to groups.",
        "explanation": "Best practices include adding users to groups and assigning roles to groups for easier management."
    },
    {
        "question": "What are two ways to generate an Event? (Choose two.)",
        "options": [
            "A. Business Rule",
            "B. Workflow",
            "C. Log entry",
            "D. Knowledge article publication"
        ],
        "answer": "A. Business Rule, B. Workflow",
        "explanation": "Events can be generated by Business Rules and Workflows in ServiceNow."
    },
    {
        "question": "Which core table in the ServiceNow platform provides a series of standard fields used on each of the tables that extend it, such as the Incident [incident] and Problem [problem] tables?",
        "options": [
            "A. Task [task]",
            "B. Assignment [assignment]",
            "C. Service [service]",
            "D. Workflow [workflow]"
        ],
        "answer": "A. Task [task]",
        "explanation": "The Task table is the core table extended by tables like Incident and Problem."
    },
    {
        "question": "Which of the following statements describes how data is organized in a table?",
        "options": [
            "A. A column is a field in the database and a record is one user",
            "B. A column is one field and a record is one row",
            "C. A column is one field and a record is one column",
            "D. A column contains data from one user and a record is one set of fields"
        ],
        "answer": "B. A column is one field and a record is one row",
        "explanation": "In a table, columns represent fields, and records represent rows."
    },
    {
        "question": "What is a sys_id?",
        "options": [
            "A. Unique 32-character identifier that is assigned to every record",
            "B. A client-side Business Rule",
            "C. A server-side Business Rule",
            "D. Unique 64-character identifier that is assigned to every record"
        ],
        "answer": "A. Unique 32-character identifier that is assigned to every record",
        "explanation": "The sys_id is a unique 32-character identifier for each record in ServiceNow."
    },
    {
        "question": "When creating a global custom table named `abc`, what is the table name that is automatically assigned by the platform?",
        "options": [
            "A. snc_abc",
            "B. abc",
            "C. u_abc",
            "D. sys_abc"
        ],
        "answer": "C. u_abc",
        "explanation": "Custom tables in ServiceNow are prefixed with 'u_' when created in the global scope."
    },
    {
        "question": "Access Control rules may provide access security for which of the following database objects?",
        "options": [
            "A. For a specific role, group, or user",
            "B. For a specific row, column, or table",
            "C. For specific groups",
            "D. For a specific CMDB Configuration item"
        ],
        "answer": "B. For a specific row, column, or table",
        "explanation": "Access Control rules provide security for rows, columns, or entire tables."
    },
    {
        "question": "What is the primary application used to load data into ServiceNow?",
        "options": [
            "A. Service Level Management",
            "B. Configuration",
            "C. System Import Sets",
            "D. System Update Sets"
        ],
        "answer": "C. System Import Sets",
        "explanation": "System Import Sets is the primary application for loading data into ServiceNow."
    },
    {
        "question": "Which of the following steps can be used to import new data into ServiceNow from a spreadsheet?",
        "options": [
            "A. Select Data Source, Schedule Transform",
            "B. Load Data, Create Transform Map, Run Transform",
            "C. Define Data Source, Select Transform Map, Run Transform",
            "D. Select Import Set, Select Transform Map, Run Transform"
        ],
        "answer": "B. Load Data, Create Transform Map, Run Transform",
        "explanation": "These are the steps to import data from a spreadsheet into ServiceNow."
    },
    {
        "question": "Which tool is used for creating dependencies between configuration items in the CMDB?",
        "options": [
            "A. CI Relationship Editor",
            "B. CMDB Builder",
            "C. CI Service Manager",
            "D. Cl Class Manager"
        ],
        "answer": "A. CI Relationship Editor",
        "explanation": "The CI Relationship Editor is used to create dependencies between configuration items in the CMDB."
    },
    {
        "question": "What is the difference between a UI Policy and Data Policy?",
        "options": [
            "A. Data Policies run when data is entered through the form, by an Import Set, or by web services, while UI Policies are set only by web services",
            "B. Data Policies can be converted into UI Policies, but UI Policies cannot be converted into Data Policies",
            "C. Data Policies run regardless of how data is entered into ServiceNow, while UI Policies are used for form interactions",
            "D. Data Policies run only after UI Policies run successfully"
        ],
        "answer": "C. Data Policies run regardless of how data is entered into ServiceNow, while UI Policies are used for form interactions",
        "explanation": "Data Policies enforce rules for all data entry methods, while UI Policies apply to form interactions."
    },
    {
        "question": "Which one of the following is an accurate list of changes that are captured in an Update Set?",
        "options": [
            "A. Changes made to: tables, forms, schedules, and client scripts",
            "B. Changes made to: tables, forms, Business Rules, and data records",
            "C. Changes made to: tables, forms, groups, and configuration items (CIs)",
            "D. Changes made to: table, forms, views, and fields"
        ],
        "answer": "D. Changes made to: table, forms, views, and fields",
        "explanation": "Update Sets capture changes to tables, forms, views, and fields."
    },
    {
        "question": "What are the steps to retrieve an Update Set?",
        "options": [
            "A. Verify Update Set is Complete, Retrieve, Preview, Apply",
            "B. Verify Update Set is Complete, Test Connection, Apply",
            "C. Verify Update Set is Complete, Test Connection, Commit",
            "D. Verify Update Set is Complete, Retrieve, Preview, Commit"
        ],
        "answer": "D. Verify Update Set is Complete, Retrieve, Preview, Commit",
        "explanation": "These are the steps to apply an Update Set to an instance."
    },
    {
        "question": "IntegrationHub enables execution of third-party APIs as a part of a flow. These integrations are referred to as",
        "options": [
            "A. an action",
            "B. a spoke",
            "C. a connection",
            "D. an integration step"
        ],
        "answer": "B. a spoke",
        "explanation": "IntegrationHub uses spokes to execute third-party APIs in a flow."
    },
    {
        "question": "Which of the following protects applications by identifying and restricting access to available files and data?",
        "options": [
            "A. Application Configuration",
            "B. Verbose Log",
            "C. Access Control Rules",
            "D. Application Scope"
        ],
        "answer": "D. Application Scope",
        "explanation": "Application Scope restricts access to files and data within an application."
    },
    {
        "question": "Which one statement correctly describes Access Control rule evaluation?",
        "options": [
            "A. Table access rules are evaluated from the general to the specific",
            "B. If more than one rule applies to a record, the older rule is evaluated first",
            "C. If a row level rule and a field level rule exist, both rules must be true before an operation is allowed",
            "D. The role with the most permissions evaluates the rules first"
        ],
        "answer": "C. If a row level rule and a field level rule exist, both rules must be true before an operation is allowed",
        "explanation": "Both row- and field-level Access Control rules must be satisfied for access."
    },
    {
        "question": "ServiceNow contains a resource which provides the following: ✑ A standard and shared set of service related definitions across ServiceNow products and platform that will enable and support true service level reporting. ✑ A CMDB framework across our products and platform that will enable and support multiple configuration strategies. What resource do these statements describe?",
        "options": [
            "A. Common Services Data Model (CSDM)",
            "B. Information Technology Service Management (ITSM)",
            "C. Configuration Management Database (CMDB)",
            "D. Information Technology Infrastructure Library (ITIL)"
        ],
        "answer": "A. Common Services Data Model (CSDM)",
        "explanation": "CSDM provides a standard framework for service-related definitions and CMDB structure."
    },
    {
        "question": "An IT manager is responsible for the Network and Hardware assignment groups, each group contains 5 team members. These team members are working on many tasks, but the manager cannot see any tasks on the Service Desk > My Groups Work list. What could explain this?",
        "options": [
            "A. The Service Desk > My Groups Work list shows active work tasks that are not yet assigned.",
            "B. The manager does not have the itil role.",
            "C. The manager is not a member of the Service Desk group.",
            "D. The manager is not a member of the Network and Hardware groups.",
            "E. The Assignment Group manager field is empty."
        ],
        "answer": "D. The manager is not a member of the Network and Hardware groups.",
        "explanation": "The manager must be a member of the groups to see tasks in the My Groups Work list."
    },
    {
        "question": "What do you need to do before you can use an Application-based trigger in your flow?",
        "options": [
            "A. Activate application trigger spoke",
            "B. Activate trigger security rules",
            "C. Activate application spoke, and plug-ins as needed",
            "D. Assign Application trigger role [sn_app_trigger_write] to SME",
            "E. Activate application plugins only"
        ],
        "answer": "C. Activate application spoke, and plug-ins as needed",
        "explanation": "Application-based triggers require activating the relevant spoke and plug-ins."
    },
    {
        "question": "The ServiceNow platform includes which types of interfaces? (Choose three.)",
        "options": [
            "A. Now Mobile Apps",
            "B. Agent Control Center",
            "C. Back Office Dashboard",
            "D. Service Portals",
            "E. Now Platform® User Interfaces",
            "F. Field Service Taskboard"
        ],
        "answer": "A. Now Mobile Apps, D. Service Portals, E. Now Platform® User Interfaces",
        "explanation": "These are valid interface types in ServiceNow."
    },
    {
        "question": "Which of the following are not included in an Update Set, by default? (Choose four.)",
        "options": [
            "A. Homepages",
            "B. Data",
            "C. Published Workflows",
            "D. Business Rules",
            "E. Schedules",
            "F. Database changes",
            "G. Related Lists",
            "H. Report Definitions",
            "I. Scheduled Jobs",
            "J. Client Scripts",
            "K. Views"
        ],
        "answer": "A. Homepages, B. Data, E. Schedules, F. Database changes",
        "explanation": "Homepages, data, schedules, and database changes are not included in Update Sets by default."
    },
    {
        "question": "You are showing your customer a new form that you have created for their new application. They would like to add a field to the form. Where could you do that? (Choose two.)",
        "options": [
            "A. Select Fields and Columns module",
            "B. Right click on form header, select Configure > Form Layout",
            "C. Click on context menu, select Configure > Form Designer",
            "D. Select Field Class Manager module"
        ],
        "answer": "B. Right click on form header, select Configure > Form Layout, C. Click on context menu, select Configure > Form Designer",
        "explanation": "These methods allow adding fields to a form in ServiceNow."
    },
    {
        "question": "Which ServiceNow resource is a framework that ensures the data your ServiceNow application requires maps correctly to the appropriate CMDB tables?",
        "options": [
            "A. Common Service Data Model (CSDM)",
            "B. Service Mapping Utility (SMU)",
            "C. Service Schema Map (SSM)",
            "D. CMDB Class Manager (CMDBCM)",
            "E. CI Class Manager (CICM)"
        ],
        "answer": "A. Common Service Data Model (CSDM)",
        "explanation": "CSDM ensures data maps correctly to CMDB tables."
    },
    {
        "question": "What do you activate when you want to add applications or functionality within your development instance?",
        "options": [
            "A. App Package",
            "B. Updated Pack",
            "C. Patch",
            "D. Plugin",
            "E. App Updated Set"
        ],
        "answer": "D. Plugin",
        "explanation": "Plugins are activated to add applications or functionality to an instance."
    },
    {
        "question": "What field contains a record's 32-character, unique identifier?",
        "options": [
            "A. sn_rec_id",
            "B. rec_id",
            "C. u_id",
            "D. sys_id",
            "E. sn_gu_id",
            "F. sn_sys_id",
            "G. id"
        ],
        "answer": "D. sys_id",
        "explanation": "The sys_id field contains a record’s 32-character unique identifier."
    },
    {
        "question": "Your company is giving all first line workers a special T-shirt as a recognition for their hard work. Management team wants a way for employees to order the T-shirt, with the ability to specify the preferred size and color. How would you ensure that only first line workers (non-managers) can submit the order?",
        "options": [
            "A. Create Record Producer and use the Available For list to specify First Line [sn_first_line] role",
            "B. Create Catalog Item and use the Not Available list to specify the Manager Group",
            "C. Create Catalog Item and use the Available For list to specify ITIL [itil] role",
            "D. Create Order Guide and use the User Criteria list to specify First Line [sn_first_line] role"
        ],
        "answer": "B. Create Catalog Item and use the Not Available list to specify the Manager Group",
        "explanation": "Using the Not Available list ensures only non-managers can access the catalog item."
    },
    {
        "question": "What is used frequently to move customizations from one instance to another?",
        "options": [
            "A. Update Sets",
            "B. Code Sets",
            "C. Update Packs",
            "D. Configuration Logs",
            "E. Remote Sets",
            "F. Local Sets",
            "G. Code Packs"
        ],
        "answer": "A. Update Sets",
        "explanation": "Update Sets are used to move customizations between ServiceNow instances."
    },
    {
        "question": "What icon do you use to change the label on a Favorite?",
        "options": [
            "A. Clock",
            "B. Hamburger",
            "C. Pencil",
            "D. Three dots",
            "E. Triangle",
            "F. Star"
        ],
        "answer": "C. Pencil",
        "explanation": "The Pencil icon is used to edit the label of a Favorite in ServiceNow."
    },
    {
        "question": "What needs to be specified, when creating a Business Rule? (Choose four.)",
        "options": [
            "A. UI action",
            "B. Table",
            "C. Fields to update",
            "D. Who can run",
            "E. Script to run",
            "F. Application scope",
            "G. Update set",
            "H. Timing",
            "I. Condition to evaluate"
        ],
        "answer": "B. Table, E. Script to run, F. Application scope, H. Timing, I. Condition to evaluate",
        "explanation": "When creating a Business Rule, you specify the table, script, application scope, timing, and condition to evaluate."
    },
    {
        "question": "What feature can track the amount of time that a task has been open, to ensure that tasks are completed within an allotted time?",
        "options": [
            "A. Task Escalation Clock",
            "B. Service Level Agreements",
            "C. Inactivity Monitor",
            "D. Response Time Clock",
            "E. Business Time Remaining"
        ],
        "answer": "B. Service Level Agreements",
        "explanation": "Service Level Agreements (SLAs) track task duration to ensure timely completion."
    },
    {
        "question": "What is a quick way to create a report from a list view?",
        "options": [
            "A. Click on filter breadcrumb, drag and drop on the Report > Create New module",
            "B. Click Funnel, define filter conditions, click Create Report",
            "C. Click Context Menu, select Create Report",
            "D. Apply filter, right click on column header, select Bar Chart",
            "E. Apply filter, right click on column header, select Create Report"
        ],
        "answer": "E. Apply filter, right click on column header, select Create Report",
        "explanation": "Right-clicking a column header and selecting Create Report is a quick way to create a report from a list view."
    },
    {
        "question": "What import utility do you use when the field names on the import set match the name of the fields on the Target table?",
        "options": [
            "A. Schema Mapping",
            "B. Automatic Mapping",
            "C. Mapping Assist",
            "D. Mapping Dashboard"
        ],
        "answer": "B. Automatic Mapping",
        "explanation": "Automatic Mapping is used when import set field names match target table field names."
    },
    {
        "question": "As an IT employee what interface would you use, if you wanted to browse internal IT documentation, like troubleshooting scripts and FAQs?",
        "options": [
            "A. Knowledge",
            "B. ServiceNow Wiki",
            "C. Knowledge Now",
            "D. SharePoint",
            "E. Stack Overflow"
        ],
        "answer": "A. Knowledge",
        "explanation": "The Knowledge application is used to browse internal IT documentation like scripts and FAQs."
    },
    {
        "question": "A new Service Desk employee in Latin America complains that the create dates and times are incorrect on their Incident list. What would you suggest to fix this issue?",
        "options": [
            "A. Have them clear their cache.",
            "B. Have them use the gear icon to set the employee's time zone.",
            "C. Recommend they use Chrome, instead of Explorer.",
            "D. Use the system properties to correct the instance's time zone.",
            "E. Have them correct the time zone on their computer."
        ],
        "answer": "B. Have them use the gear icon to set the employee's time zone.",
        "explanation": "Setting the correct time zone via the gear icon adjusts the display of dates and times for the user."
    },
    {
        "question": "What are three security modules often used by the System Administrator? (Choose three.)",
        "options": [
            "A. System Properties > Security",
            "B. Utilities > Migrate Security",
            "C. System Security > Security",
            "D. Self-Service > My Access",
            "E. System Security > Access Control (ACL)",
            "F. Password Management > Security Questions",
            "G. System Security > High Security Settings"
        ],
        "answer": "A. System Properties > Security, E. System Security > Access Control (ACL), G. System Security > High Security Settings",
        "explanation": "These modules are commonly used by System Administrators to manage security settings."
    },
    {
        "question": "When testing a catalog item, having a manager approval flows, which of these best practices would you follow? (Choose three.)",
        "options": [
            "A. Make sure the latest flows are activated.",
            "B. Use the instance Incognito setting to quickly toggle between requester and approver.",
            "C. Impersonate the requester to ensure the form works.",
            "D. Make sure the requester's user record has a manager specified.",
            "E. Create and select your Testing Update Set, before starting the test cases.",
            "F. Use your Admin account, so you can approve the items quickly."
        ],
        "answer": "A. Make sure the latest flows are activated., C. Impersonate the requester to ensure the form works., D. Make sure the requester's user record has a manager specified.",
        "explanation": "These best practices ensure proper testing of catalog items with approval flows."
    },
    {
        "question": "What is a no-code approach to control the mandatory or read-only state of a form field?",
        "options": [
            "A. UI Action",
            "B. Client Script",
            "C. UI Script",
            "D. UI Rule",
            "E. UI Policy"
        ],
        "answer": "E. UI Policy",
        "explanation": "UI Policies provide a no-code approach to control field states like mandatory or read-only on forms."
    },
    {
        "question": "When moving multiple update sets at one time, what might you do to facilitate the move?",
        "options": [
            "A. Batch",
            "B. Verify",
            "C. Test",
            "D. Preview"
        ],
        "answer": "A. Batch",
        "explanation": "Batching multiple Update Sets facilitates moving them together."
    },
    {
        "question": "What is specified in an Access Control rule?",
        "options": [
            "A. Groups, Conditional Expressions and Workflows",
            "B. Table Schema, CRUD, and User Authentication",
            "C. Object and Operation being secured; Permissions required to access the object",
            "D. security_admin"
        ],
        "answer": "C. Object and Operation being secured; Permissions required to access the object",
        "explanation": "Access Control rules specify the object, operation, and required permissions."
    },
    {
        "question": "Which icon would you double click, to expand and collapse the list of all Applications and Modules?",
        "options": [
            "A. Star",
            "B. Clock",
            "C. Application",
            "D. Funnel"
        ],
        "answer": "C. Application",
        "explanation": "Double-clicking the Application icon in the Application Navigator expands or collapses the list."
    },
    {
        "question": "What do you call any component that needs to be managed in order to deliver services?",
        "options": [
            "A. CSDM Items",
            "B. CMDB",
            "C. Configuration item",
            "D. Service Offerings",
            "E. Asset"
        ],
        "answer": "C. Configuration item",
        "explanation": "Configuration Items (CIs) are components managed in the CMDB to deliver services."
    },
    {
        "question": "A new service catalog item is being developed, but should only be visible to managers inside the HR Department. What method would you use to fulfill this requirement?",
        "options": [
            "A. Specify the Dept_Mgr role on the catalog content block",
            "B. Add the Department Manager group to the catalog item's user criteria",
            "C. Add the Department Manager group to the catalog item's ACL",
            "D. Only publish the item in the HR service catalog",
            "E. Use a Dept_Mgr ACL on the HR service catalog"
        ],
        "answer": "B. Add the Department Manager group to the catalog item's user criteria",
        "explanation": "User Criteria on the catalog item restricts visibility to the Department Manager group."
    },
    {
        "question": "A user wants to create a set of filter conditions, where they want to show records which satisfy two conditions: Incidents where the state is Closed; Incidents where Assignment Group is Network. After clicking the Funnel icon, what should the user do?",
        "options": [
            "A. Define the first condition; click AND button; define second condition; click Run",
            "B. Define the first condition; click AND button; define second condition; press enter",
            "C. Define the first condition; click OR button; define second condition; press enter",
            "D. Define the first condition; click > icon on breadcrumb, define second condition; click Run",
            "E. Define the first condition; click > icon on breadcrumb, define second condition; press enter"
        ],
        "answer": "A. Define the first condition; click AND button; define second condition; click Run",
        "explanation": "To filter for both conditions, use AND to combine them and click Run to apply the filter."
    },
    {
        "question": "Access Control rules are applied to a specific table, like the Incident table. What is the object name for a rule that is specific to the Incident table and the Major Incident field?",
        "options": [
            "A. Incident.Major_Incident",
            "B. incident=>major_incident",
            "C. incident<=>major_incident",
            "D. incident||major_incident",
            "E. incident.major_incident"
        ],
        "answer": "E. incident.major_incident",
        "explanation": "The object name for a field-specific ACL uses dot notation: table.field."
    },
    {
        "question": "Two departments (HR Onboarding and Facilities) have come to you, asking for a way for employees to request event room set up services. The requirements are the same for the form and the task routing to the Facilities' assignment group. For HR, the item will be used primarily for the Onboarding coordinators, for employee orientation sessions. For Facilities, the item will be used for anyone in the company who needs room set up services. However, both departments have their own service catalogs. What do you do, to support these requirements?",
        "options": [
            "A. Create one Catalog Item for HR Event Room Set Up and one for Facilities Event Room Set Up; then publish each to the appropriate Catalog.",
            "B. Create one Catalog Item for Event Room Set Up; then publish to both Catalogs.",
            "C. Create one Catalog Item for Event Room Set Up; then publish to the Parent Catalog, which is accessible to both HR and Facilities.",
            "D. Create one Catalog Item for Event Room Set Up; then use ACLs to control access."
        ],
        "answer": "B. Create one Catalog Item for Event Room Set Up; then publish to both Catalogs.",
        "explanation": "A single Catalog Item can be published to both HR and Facilities catalogs, with User Criteria to control access for HR coordinators."
    },
    {
        "question": "After finishing your work on High Security Settings, what do you do to return to normal admin security levels?",
        "options": [
            "A. Select Normal role",
            "B. Log out and back in",
            "C. Use System Administration > Normal Security module",
            "D. Select Global Update Set",
            "E. End Impersonation"
        ],
        "answer": "B. Log out and back in",
        "explanation": "Logging out and back in resets the elevated security role to normal admin levels."
    },
    {
        "question": "What type of field allows you to look up values from one other table?",
        "options": [
            "A. Reference",
            "B. Verity",
            "C. Options",
            "D. Selections",
            "E. Dot walk",
            "F. Lookup"
        ],
        "answer": "A. Reference",
        "explanation": "Reference fields allow looking up values from another table in ServiceNow."
    },
    {
        "question": "Which module would you use to create a new automation of business logic such as approvals, tasks, and notifications?",
        "options": [
            "A. Process Automation > Flow Designer",
            "B. Process Automation > Flow Administration",
            "C. Process Automation > Workflow Editor",
            "D. Process Automation > Process Flow",
            "E. Process Automation > Active Flows"
        ],
        "answer": "A. Process Automation > Flow Designer",
        "explanation": "Flow Designer is used to create automations for business logic like approvals, tasks, and notifications."
    },
    {
        "question": "A department manager asks an analyst to build some reports. Where do you recommend the analyst start?",
        "options": [
            "A. Report Dashboard > Create New",
            "B. Reports > Getting Started",
            "C. Performance Analytics > Reports",
            "D. Self-Service > Reports",
            "E. Reports > Create New"
        ],
        "answer": "E. Reports > Create New",
        "explanation": "The Reports > Create New module is the starting point for building reports."
    },
    {
        "question": "What are the steps for applying an update set to an instance?",
        "options": [
            "A. Retrieve, Preview, Commit",
            "B. Specify, Transform, Apply",
            "C. Retrieve, Assess, Apply",
            "D. Get, Test, Push",
            "E. Pull, Review, Push"
        ],
        "answer": "A. Retrieve, Preview, Commit",
        "explanation": "These are the steps to apply an Update Set to an instance."
    },
    {
        "question": "When importing spreadsheet data into ServiceNow, in which step does the data get written to the receiving table?",
        "options": [
            "A. Run Transform",
            "B. Run Import",
            "C. Import Dataset",
            "D. Execute Transform",
            "E. Schedule Transform"
        ],
        "answer": "A. Run Transform",
        "explanation": "Data is written to the receiving table during the Run Transform step."
    },
    {
        "question": "What would you do, on a list, if you wanted to show the records in groups, based on the column category? (Choose two.)",
        "options": [
            "A. On list Context Menu, select Group By > Category",
            "B. On the Filter Menu, select Group By > Category",
            "C. Click Group On icon, select Category",
            "D. On Navigator Filter, type tablename.group.category and press enter",
            "E. On the Category column title, click Context menu > Group By Category"
        ],
        "answer": "A. On list Context Menu, select Group By > Category, E. On the Category column title, click Context menu > Group By Category",
        "explanation": "These methods allow grouping records by the Category column in a list view."
    },
    {
        "question": "Which collaboration tool is available from the banner, using the bubble icon?",
        "options": [
            "A. Now Messenger",
            "B. Agent Chat",
            "C. Connect Chat",
            "D. Collaborate Now",
            "E. Live Feed"
        ],
        "answer": "C. Connect Chat",
        "explanation": "Connect Chat is accessed via the bubble icon in the banner for real-time collaboration."
    },
    {
        "question": "On the knowledge base record, which tab would you use to define which users are not able to write articles to the knowledge base?",
        "options": [
            "A. Can Contribute",
            "B. Cannot Author",
            "C. Cannot Contribute",
            "D. Cannot Write",
            "E. Read Only"
        ],
        "answer": "C. Cannot Contribute",
        "explanation": "The Cannot Contribute tab defines users who cannot write articles to the knowledge base."
    },
    {
        "question": "Which features allow you to update multiple records at one time? (Choose two.)",
        "options": [
            "A. List Editor",
            "B. Field Update Action",
            "C. Bulk Record Update",
            "D. Data Remediation Dashboard",
            "E. Update Selected Action"
        ],
        "answer": "A. List Editor, E. Update Selected Action",
        "explanation": "The List Editor and Update Selected Action allow updating multiple records simultaneously."
    },
    {
        "question": "Categories in the knowledge base, by default, can be created and edited by which knowledge workers? (Choose two.)",
        "options": [
            "A. Knowledge Authors",
            "B. Knowledge Contributors",
            "C. Knowledge Controller",
            "D. Knowledge Managers",
            "E. Knowledge Category Managers",
            "F. Knowledge Submitters",
            "G. Knowledge Owners",
            "H. Knowledge Taxonomy Owner"
        ],
        "answer": "D. Knowledge Managers, G. Knowledge Owners",
        "explanation": "Knowledge Managers and Knowledge Owners can create and edit categories by default."
    },
    {
        "question": "Which collaboration tool opens a sidebar and allows you to create new conversations with other ServiceNow users?",
        "options": [
            "A. Skype Now",
            "B. Collaborate Now",
            "C. Agent Messenger",
            "D. Agent Chat",
            "E. Connect Chat"
        ],
        "answer": "E. Connect Chat",
        "explanation": "Connect Chat opens a sidebar for creating new conversations with ServiceNow users."
    },
    {
        "question": "What module would you use if you wanted to view a list of all of the fields on the Incident table? (Choose two.)",
        "options": [
            "A. Tables & Columns",
            "B. Dictionary",
            "C. Data Class Manager",
            "D. Dictionary Dashboard",
            "E. Database View",
            "F. Schema"
        ],
        "answer": "A. Tables & Columns, B. Dictionary",
        "explanation": "The Tables & Columns and Dictionary modules display all fields on the Incident table."
    },
    {
        "question": "What component causes a flow to run after a record has been created or updated?",
        "options": [
            "A. Date-based trigger",
            "B. On-change trigger",
            "C. Record-based trigger",
            "D. Application-based trigger",
            "E. Updated-date trigger"
        ],
        "answer": "C. Record-based trigger",
        "explanation": "A Record-based trigger initiates a flow when a record is created or updated."
    },
    {
        "question": "What type of field is Boolean and appears as a check box?",
        "options": [
            "A. Yes/No",
            "B. True/False",
            "C. On/Off",
            "D. Binary",
            "E. 0/1"
        ],
        "answer": "B. True/False",
        "explanation": "A Boolean field in ServiceNow is a True/False field displayed as a checkbox."
    },
    {
        "question": "Which module is used to access the knowledge bases which are available to you?",
        "options": [
            "A. Knowledge > Home",
            "B. Self Service > Knowledge",
            "C. Knowledge > All",
            "D. Knowledge > Knowledge Bases",
            "E. Knowledge > Overview"
        ],
        "answer": "D. Knowledge > Knowledge Bases",
        "explanation": "The Knowledge > Knowledge Bases module allows users to access and manage the knowledge bases available to them."
    },
    {
        "question": "Which feature allows you to automate business processes without writing code?",
        "options": [
            "A. Flow Designer",
            "B. Script Includes",
            "C. Business Rules",
            "D. Client Scripts"
        ],
        "answer": "A. Flow Designer",
        "explanation": "Flow Designer provides a no-code interface to automate business processes using triggers, actions, and flows."
    },
    {
        "question": "What is the purpose of the ServiceNow Service Portal?",
        "options": [
            "A. To manage server-side scripts",
            "B. To provide a user-friendly interface for end users",
            "C. To configure database schemas",
            "D. To manage system logs"
        ],
        "answer": "B. To provide a user-friendly interface for end users",
        "explanation": "The Service Portal offers a customizable, user-friendly interface for end users to access services and knowledge."
    },
    {
        "question": "Which table stores information about ServiceNow groups?",
        "options": [
            "A. sys_user",
            "B. sys_user_group",
            "C. sys_group",
            "D. sys_role_group"
        ],
        "answer": "B. sys_user_group",
        "explanation": "The sys_user_group table stores information about groups in ServiceNow."
    },
    {
        "question": "What is the purpose of a UI Policy Action?",
        "options": [
            "A. To execute server-side scripts",
            "B. To control field properties on a form",
            "C. To trigger notifications",
            "D. To manage user roles"
        ],
        "answer": "B. To control field properties on a form",
        "explanation": "UI Policy Actions define how fields behave (e.g., mandatory, read-only) on a form based on conditions."
    },
    {
        "question": "Which role is required to create or modify Access Control Lists (ACLs)?",
        "options": [
            "A. itil",
            "B. admin",
            "C. security_admin",
            "D. acl_admin"
        ],
        "answer": "C. security_admin",
        "explanation": "The security_admin role is required to create or modify ACLs in ServiceNow."
    },
    {
        "question": "What is the purpose of the 'Reference Qualifier' field in a reference field configuration?",
        "options": [
            "A. To define the table for the reference field",
            "B. To filter the records displayed in the reference lookup",
            "C. To set the default value for the field",
            "D. To make the field mandatory"
        ],
        "answer": "B. To filter the records displayed in the reference lookup",
        "explanation": "Reference Qualifiers filter the records shown in a reference field’s lookup list."
    },
    {
        "question": "Which module allows you to view all active incidents assigned to your groups?",
        "options": [
            "A. Incident > My Work",
            "B. Incident > Assigned to Me",
            "C. Incident > My Groups Work",
            "D. Incident > Open"
        ],
        "answer": "C. Incident > My Groups Work",
        "explanation": "The Incident > My Groups Work module displays incidents assigned to the user’s groups."
    },
    {
        "question": "What is the purpose of the 'Transform Map' in an import process?",
        "options": [
            "A. To load data into the import set table",
            "B. To map fields from the import set to the target table",
            "C. To schedule the import process",
            "D. To validate the data before import"
        ],
        "answer": "B. To map fields from the import set to the target table",
        "explanation": "Transform Maps define how fields in the import set table map to fields in the target table."
    },
    {
        "question": "Which of the following is a benefit of using Flow Designer over Workflow Editor?",
        "options": [
            "A. Requires extensive scripting knowledge",
            "B. Supports no-code process automation",
            "C. Only works with server-side scripts",
            "D. Limited to incident management"
        ],
        "answer": "B. Supports no-code process automation",
        "explanation": "Flow Designer allows no-code automation, making it more accessible than the Workflow Editor."
    },
    {
        "question": "What is the purpose of the 'My Favorites' section in the Application Navigator?",
        "options": [
            "A. To store frequently accessed reports",
            "B. To bookmark frequently used modules or applications",
            "C. To save search queries",
            "D. To manage user roles"
        ],
        "answer": "B. To bookmark frequently used modules or applications",
        "explanation": "My Favorites allows users to bookmark modules or applications for quick access."
    },
    {
        "question": "Which field type allows users to select multiple values from a predefined list?",
        "options": [
            "A. Choice",
            "B. List",
            "C. Reference",
            "D. Multi-Select"
        ],
        "answer": "B. List",
        "explanation": "The List field type allows users to select multiple values from a predefined list."
    },
    {
        "question": "What is the purpose of the 'Condition Builder' in ServiceNow?",
        "options": [
            "A. To create database tables",
            "B. To define filter conditions for lists and reports",
            "C. To write server-side scripts",
            "D. To configure UI actions"
        ],
        "answer": "B. To define filter conditions for lists and reports",
        "explanation": "The Condition Builder is used to create filter conditions for lists, reports, or other queries."
    },
    {
        "question": "Which module is used to configure SLAs for incident management?",
        "options": [
            "A. SLA > Definitions",
            "B. SLA > Configurations",
            "C. SLA > Setup",
            "D. SLA > Management"
        ],
        "answer": "A. SLA > Definitions",
        "explanation": "The SLA > Definitions module is used to configure Service Level Agreements for incident management."
    },
    {
        "question": "What is the purpose of the 'sys_audit' table in ServiceNow?",
        "options": [
            "A. To store user authentication logs",
            "B. To track changes to records",
            "C. To manage system configurations",
            "D. To store event logs"
        ],
        "answer": "B. To track changes to records",
        "explanation": "The sys_audit table tracks changes to records for auditing purposes."
    },
    {
        "question": "Which role allows a user to manage knowledge articles?",
        "options": [
            "A. knowledge",
            "B. itil",
            "C. knowledge_admin",
            "D. article_manager"
        ],
        "answer": "C. knowledge_admin",
        "explanation": "The knowledge_admin role allows users to manage knowledge articles."
    },
    {
        "question": "What is the purpose of the 'Homepage' feature in ServiceNow?",
        "options": [
            "A. To display dashboards with widgets",
            "B. To manage user groups",
            "C. To configure system properties",
            "D. To create new tables"
        ],
        "answer": "A. To display dashboards with widgets",
        "explanation": "Homepages display dashboards with widgets for quick access to key information."
    },
    {
        "question": "Which of the following is true about ServiceNow’s Knowledge Management?",
        "options": [
            "A. Only admins can create knowledge articles",
            "B. Knowledge articles are stored in the kb_knowledge table",
            "C. Knowledge articles cannot be versioned",
            "D. Knowledge bases are not searchable"
        ],
        "answer": "B. Knowledge articles are stored in the kb_knowledge table",
        "explanation": "Knowledge articles are stored in the kb_knowledge table and can be managed by users with appropriate roles."
    },
    {
        "question": "What is the purpose of a 'GlideRecord' in ServiceNow scripting?",
        "options": [
            "A. To create UI actions",
            "B. To query and manipulate database records",
            "C. To manage user authentication",
            "D. To configure workflows"
        ],
        "answer": "B. To query and manipulate database records",
        "explanation": "GlideRecord is a server-side API used to query and manipulate records in the ServiceNow database."
    },
    {
        "question": "Which module allows you to view all active workflows?",
        "options": [
            "A. Workflow > Active Workflows",
            "B. Workflow > Editor",
            "C. Workflow > Status",
            "D. Workflow > Dashboard"
        ],
        "answer": "A. Workflow > Active Workflows",
        "explanation": "The Workflow > Active Workflows module lists all currently active workflows."
    },
    {
        "question": "What is the purpose of the 'sys_trigger' table?",
        "options": [
            "A. To store scheduled jobs",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store scheduled jobs",
        "explanation": "The sys_trigger table stores scheduled jobs, such as those for reports or scripts."
    },
    {
        "question": "Which feature allows you to create reusable scripts that can be called from other scripts?",
        "options": [
            "A. Script Include",
            "B. Client Script",
            "C. UI Script",
            "D. Business Rule"
        ],
        "answer": "A. Script Include",
        "explanation": "Script Includes are reusable server-side scripts that can be called from other scripts."
    },
    {
        "question": "What is the purpose of the 'sys_properties' table?",
        "options": [
            "A. To store system configuration settings",
            "B. To manage user roles",
            "C. To track record changes",
            "D. To store knowledge articles"
        ],
        "answer": "A. To store system configuration settings",
        "explanation": "The sys_properties table stores system-wide configuration settings."
    },
    {
        "question": "Which role is required to activate a plugin in ServiceNow?",
        "options": [
            "A. itil",
            "B. admin",
            "C. plugin_admin",
            "D. system_admin"
        ],
        "answer": "B. admin",
        "explanation": "The admin role is required to activate plugins in ServiceNow."
    },
    {
        "question": "What is the purpose of the 'Dependency View' in the CMDB?",
        "options": [
            "A. To display relationships between configuration items",
            "B. To manage user permissions",
            "C. To create new tables",
            "D. To schedule reports"
        ],
        "answer": "A. To display relationships between configuration items",
        "explanation": "The Dependency View shows relationships between configuration items in the CMDB."
    },
    {
        "question": "Which module is used to create new roles in ServiceNow?",
        "options": [
            "A. System Security > Roles",
            "B. User Administration > Roles",
            "C. System Properties > Roles",
            "D. Security Operations > Roles"
        ],
        "answer": "B. User Administration > Roles",
        "explanation": "The User Administration > Roles module is used to create and manage roles."
    },
    {
        "question": "What is the purpose of the 'sys_dictionary' table?",
        "options": [
            "A. To store field definitions for tables",
            "B. To manage user groups",
            "C. To track system events",
            "D. To store scheduled jobs"
        ],
        "answer": "A. To store field definitions for tables",
        "explanation": "The sys_dictionary table contains metadata about table fields."
    },
    {
        "question": "Which feature allows you to automate notifications based on specific events?",
        "options": [
            "A. Notification Rules",
            "B. Event Rules",
            "C. Workflow Notifications",
            "D. Notification Triggers"
        ],
        "answer": "A. Notification Rules",
        "explanation": "Notification Rules automate notifications based on specific events or conditions."
    },
    {
        "question": "What is the purpose of the 'sys_user_role' table?",
        "options": [
            "A. To store user records",
            "B. To store role definitions",
            "C. To manage group memberships",
            "D. To track audit logs"
        ],
        "answer": "B. To store role definitions",
        "explanation": "The sys_user_role table stores definitions of roles in ServiceNow."
    },
    {
        "question": "Which module is used to manage Service Catalog categories?",
        "options": [
            "A. Service Catalog > Maintain Categories",
            "B. Service Catalog > Categories",
            "C. Service Catalog > Catalog Management",
            "D. Service Catalog > Category Editor"
        ],
        "answer": "A. Service Catalog > Maintain Categories",
        "explanation": "The Service Catalog > Maintain Categories module is used to manage catalog categories."
    },
    {
        "question": "What is the purpose of a 'Client Script' in ServiceNow?",
        "options": [
            "A. To execute server-side logic",
            "B. To control form behavior on the client side",
            "C. To manage database tables",
            "D. To schedule reports"
        ],
        "answer": "B. To control form behavior on the client side",
        "explanation": "Client Scripts run on the client side to control form behavior, such as field validation."
    },
    {
        "question": "Which feature allows you to group related catalog items for streamlined ordering?",
        "options": [
            "A. Record Producer",
            "B. Order Guide",
            "C. Catalog Item",
            "D. Workflow"
        ],
        "answer": "B. Order Guide",
        "explanation": "Order Guides group related catalog items for streamlined ordering."
    },
    {
        "question": "What is the purpose of the 'sys_log' table?",
        "options": [
            "A. To store system logs",
            "B. To manage user roles",
            "C. To track record changes",
            "D. To store knowledge articles"
        ],
        "answer": "A. To store system logs",
        "explanation": "The sys_log table stores system logs for troubleshooting and monitoring."
    },
    {
        "question": "Which role allows a user to create and manage reports?",
        "options": [
            "A. report_user",
            "B. report_admin",
            "C. itil",
            "D. admin"
        ],
        "answer": "B. report_admin",
        "explanation": "The report_admin role allows users to create and manage reports."
    },
    {
        "question": "What is the purpose of the 'ServiceNow Mobile App'?",
        "options": [
            "A. To manage server configurations",
            "B. To provide mobile access to ServiceNow functionality",
            "C. To create database schemas",
            "D. To schedule system backups"
        ],
        "answer": "B. To provide mobile access to ServiceNow functionality",
        "explanation": "The ServiceNow Mobile App allows users to access platform functionality on mobile devices."
    },
    {
        "question": "Which module is used to view all active SLAs?",
        "options": [
            "A. SLA > Active SLAs",
            "B. SLA > Dashboard",
            "C. SLA > Overview",
            "D. SLA > Status"
        ],
        "answer": "A. SLA > Active SLAs",
        "explanation": "The SLA > Active SLAs module displays all currently active Service Level Agreements."
    },
    {
        "question": "What is the purpose of a 'Data Policy' in ServiceNow?",
        "options": [
            "A. To enforce field rules for all data entry methods",
            "B. To manage user authentication",
            "C. To create UI actions",
            "D. To schedule reports"
        ],
        "answer": "A. To enforce field rules for all data entry methods",
        "explanation": "Data Policies enforce field rules for data entered via forms, imports, or web services."
    },
    {
        "question": "Which feature allows you to create a visual representation of a business process?",
        "options": [
            "A. Flow Designer",
            "B. Workflow Editor",
            "C. Process Designer",
            "D. Visual Task Board"
        ],
        "answer": "B. Workflow Editor",
        "explanation": "The Workflow Editor creates visual representations of business processes."
    },
    {
        "question": "What is the purpose of the 'sys_email' table?",
        "options": [
            "A. To store email notifications",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store email notifications",
        "explanation": "The sys_email table stores email notifications sent by ServiceNow."
    },
    {
        "question": "Which role is required to manage Service Catalog items?",
        "options": [
            "A. catalog_admin",
            "B. itil",
            "C. service_admin",
            "D. admin"
        ],
        "answer": "A. catalog_admin",
        "explanation": "The catalog_admin role is required to manage Service Catalog items."
    },
    {
        "question": "What is the purpose of the 'Business Service Map' in ServiceNow?",
        "options": [
            "A. To display relationships between business services and CIs",
            "B. To manage user groups",
            "C. To create new tables",
            "D. To schedule reports"
        ],
        "answer": "A. To display relationships between business services and CIs",
        "explanation": "The Business Service Map shows relationships between business services and configuration items."
    },
    {
        "question": "Which module is used to manage user groups?",
        "options": [
            "A. User Administration > Groups",
            "B. System Security > Groups",
            "C. System Properties > Groups",
            "D. Group Management > Groups"
        ],
        "answer": "A. User Administration > Groups",
        "explanation": "The User Administration > Groups module is used to manage user groups."
    },
    {
        "question": "What is the purpose of the 'sys_created_by' field?",
        "options": [
            "A. To store the user who created a record",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store the user who created a record",
        "explanation": "The sys_created_by field stores the username of the user who created a record."
    },
    {
        "question": "Which feature allows you to create dynamic filters for reference fields?",
        "options": [
            "A. Dynamic Reference Qualifier",
            "B. Filter Conditions",
            "C. Dynamic Lookup",
            "D. Reference Filter"
        ],
        "answer": "A. Dynamic Reference Qualifier",
        "explanation": "Dynamic Reference Qualifiers create dynamic filters for reference fields."
    },
    {
        "question": "What is the purpose of the 'sys_updated_on' field?",
        "options": [
            "A. To store the date and time a record was last updated",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store the date and time a record was last updated",
        "explanation": "The sys_updated_on field records the date and time a record was last updated."
    },
    {
        "question": "Which module is used to view all active notifications?",
        "options": [
            "A. System Notification > Notifications",
            "B. System Notification > Active Notifications",
            "C. System Notification > Email",
            "D. System Notification > Dashboard"
        ],
        "answer": "A. System Notification > Notifications",
        "explanation": "The System Notification > Notifications module lists all active notifications."
    },
    {
        "question": "What is the purpose of the 'GlideSystem' class in ServiceNow scripting?",
        "options": [
            "A. To manage user authentication",
            "B. To access system-level functions and properties",
            "C. To create UI actions",
            "D. To manage database tables"
        ],
        "answer": "B. To access system-level functions and properties",
        "explanation": "The GlideSystem class provides access to system-level functions and properties in scripts."
    },
    {
        "question": "Which feature allows you to create a custom application in ServiceNow?",
        "options": [
            "A. Application Creator",
            "B. Studio",
            "C. App Engine",
            "D. Application Designer"
        ],
        "answer": "B. Studio",
        "explanation": "ServiceNow Studio is used to create and manage custom applications."
    },
    {
        "question": "What is the purpose of the 'sys_updated_by' field?",
        "options": [
            "A. To store the user who last updated a record",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store the user who last updated a record",
        "explanation": "The sys_updated_by field stores the username of the user who last updated a record."
    },
    {
        "question": "Which module is used to manage system properties?",
        "options": [
            "A. System Properties > Administration",
            "B. System Properties > System",
            "C. System Properties > All",
            "D. System Properties > Management"
        ],
        "answer": "B. System Properties > System",
        "explanation": "The System Properties > System module is used to manage system properties."
    },
    {
        "question": "What is the purpose of the 'Visual Task Board' in ServiceNow?",
        "options": [
            "A. To manage database schemas",
            "B. To provide a visual interface for task management",
            "C. To create UI actions",
            "D. To schedule reports"
        ],
        "answer": "B. To provide a visual interface for task management",
        "explanation": "Visual Task Boards provide a visual, Kanban-style interface for managing tasks."
    },
    {
        "question": "Which role is required to create custom tables in ServiceNow?",
        "options": [
            "A. table_admin",
            "B. admin",
            "C. itil",
            "D. schema_admin"
        ],
        "answer": "B. admin",
        "explanation": "The admin role is required to create custom tables in ServiceNow."
    },
    {
        "question": "What is the purpose of the 'sys_created_on' field?",
        "options": [
            "A. To store the date and time a record was created",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store the date and time a record was created",
        "explanation": "The sys_created_on field records the date and time a record was created."
    },
    {
        "question": "Which module is used to manage ServiceNow plugins?",
        "options": [
            "A. System Definition > Plugins",
            "B. System Definition > Modules",
            "C. System Definition > Applications",
            "D. System Definition > Management"
        ],
        "answer": "A. System Definition > Plugins",
        "explanation": "The System Definition > Plugins module is used to manage plugins."
    },
    {
        "question": "What is the purpose of the 'ServiceNow Agent' mobile app?",
        "options": [
            "A. To manage server configurations",
            "B. To provide mobile access for IT agents",
            "C. To create database schemas",
            "D. To schedule system backups"
        ],
        "answer": "B. To provide mobile access for IT agents",
        "explanation": "The ServiceNow Agent app provides mobile access for IT agents to manage tasks."
    },
    {
        "question": "Which feature allows you to create a custom dashboard?",
        "options": [
            "A. Dashboard Creator",
            "B. Performance Analytics",
            "C. Reports > Dashboard",
            "D. Homepages"
        ],
        "answer": "D. Homepages",
        "explanation": "Homepages allow users to create custom dashboards with widgets."
    },
    {
        "question": "What is the purpose of the 'sys_security_acl' table?",
        "options": [
            "A. To store Access Control Lists",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store Access Control Lists",
        "explanation": "The sys_security_acl table stores Access Control Lists for security rules."
    },
    {
        "question": "Which module is used to view all active users in ServiceNow?",
        "options": [
            "A. User Administration > Users",
            "B. System Security > Users",
            "C. System Properties > Users",
            "D. User Management > Users"
        ],
        "answer": "A. User Administration > Users",
        "explanation": "The User Administration > Users module lists all active users."
    },
    {
        "question": "What is the purpose of the 'GlideDateTime' class in ServiceNow scripting?",
        "options": [
            "A. To manage date and time operations",
            "B. To create UI actions",
            "C. To manage user authentication",
            "D. To configure workflows"
        ],
        "answer": "A. To manage date and time operations",
        "explanation": "The GlideDateTime class is used for date and time operations in scripts."
    },
    {
        "question": "Which feature allows you to create a custom application scope?",
        "options": [
            "A. Application Creator",
            "B. Studio",
            "C. App Engine",
            "D. Scope Manager"
        ],
        "answer": "B. Studio",
        "explanation": "ServiceNow Studio allows the creation of custom application scopes."
    },
    {
        "question": "What is the purpose of the 'sys_user_has_role' table?",
        "options": [
            "A. To store user-role assignments",
            "B. To manage user groups",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store user-role assignments",
        "explanation": "The sys_user_has_role table stores assignments of roles to users."
    },
    {
        "question": "Which module is used to manage Service Catalog variables?",
        "options": [
            "A. Service Catalog > Maintain Variables",
            "B. Service Catalog > Variables",
            "C. Service Catalog > Variable Editor",
            "D. Service Catalog > Variable Management"
        ],
        "answer": "B. Service Catalog > Variables",
        "explanation": "The Service Catalog > Variables module is used to manage catalog variables."
    },
    {
        "question": "What is the purpose of the 'sys_db_object' table?",
        "options": [
            "A. To store table definitions",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store table definitions",
        "explanation": "The sys_db_object table stores definitions of database tables."
    },
    {
        "question": "Which feature allows you to create automated tests for ServiceNow applications?",
        "options": [
            "A. Automated Test Framework",
            "B. Test Designer",
            "C. Test Manager",
            "D. Application Tester"
        ],
        "answer": "A. Automated Test Framework",
        "explanation": "The Automated Test Framework (ATF) allows creation of automated tests for applications."
    },
    {
        "question": "What is the purpose of the 'sys_script' table?",
        "options": [
            "A. To store Business Rules",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store Business Rules",
        "explanation": "The sys_script table stores Business Rules in ServiceNow."
    },
    {
        "question": "Which module is used to manage ServiceNow workflows?",
        "options": [
            "A. Workflow > Editor",
            "B. Workflow > Management",
            "C. Workflow > Designer",
            "D. Workflow > Administration"
        ],
        "answer": "A. Workflow > Editor",
        "explanation": "The Workflow > Editor module is used to create and manage workflows."
    },
    {
        "question": "What is the purpose of the 'sys_ui_action' table?",
        "options": [
            "A. To store UI Actions",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store UI Actions",
        "explanation": "The sys_ui_action table stores UI Actions like buttons and form links."
    },
    {
        "question": "Which feature allows you to create a custom report type?",
        "options": [
            "A. Report Designer",
            "B. Report Builder",
            "C. Report Types",
            "D. Custom Reports"
        ],
        "answer": "C. Report Types",
        "explanation": "The Report Types module allows creation of custom report types."
    },
    {
        "question": "What is the purpose of the 'sys_client_script' table?",
        "options": [
            "A. To store Client Scripts",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store Client Scripts",
        "explanation": "The sys_client_script table stores Client Scripts for form interactions."
    },
    {
        "question": "Which module is used to manage ServiceNow notifications?",
        "options": [
            "A. System Notification > Email",
            "B. System Notification > Notifications",
            "C. System Notification > Alerts",
            "D. System Notification > Management"
        ],
        "answer": "B. System Notification > Notifications",
        "explanation": "The System Notification > Notifications module is used to manage notifications."
    },
    {
        "question": "What is the purpose of the 'sys_ui_policy' table?",
        "options": [
            "A. To store UI Policies",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store UI Policies",
        "explanation": "The sys_ui_policy table stores UI Policies for controlling form behavior."
    },
    {
        "question": "Which feature allows you to create a custom table in ServiceNow Studio?",
        "options": [
            "A. Table Creator",
            "B. Table Builder",
            "C. Table Designer",
            "D. Table Manager"
        ],
        "answer": "C. Table Designer",
        "explanation": "The Table Designer in Studio allows creation of custom tables."
    },
    {
        "question": "What is the purpose of the 'sys_script_include' table?",
        "options": [
            "A. To store Script Includes",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store Script Includes",
        "explanation": "The sys_script_include table stores Script Includes for reusable scripts."
    },
    {
        "question": "Which module is used to view all active roles in ServiceNow?",
        "options": [
            "A. User Administration > Roles",
            "B. System Security > Roles",
            "C. System Properties > Roles",
            "D. Role Management > Roles"
        ],
        "answer": "A. User Administration > Roles",
        "explanation": "The User Administration > Roles module lists all active roles."
    },
    {
        "question": "What is the purpose of the 'sys_event' table?",
        "options": [
            "A. To store system events",
            "B. To manage user roles",
            "C. To track record changes",
            "D. To store audit logs"
        ],
        "answer": "A. To store system events",
        "explanation": "The sys_event table stores system events triggered in ServiceNow."
    },
    {
        "question": "Which feature allows you to create a custom Service Portal widget?",
        "options": [
            "A. Widget Creator",
            "B. Service Portal Designer",
            "C. Widget Editor",
            "D. Portal Builder"
        ],
        "answer": "C. Widget Editor",
        "explanation": "The Widget Editor in Service Portal allows creation of custom widgets."
    },
    {
        "question": "What is the purpose of the 'sys_ui_script' table?",
        "options": [
            "A. To store UI Scripts",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store UI Scripts",
        "explanation": "The sys_ui_script table stores UI Scripts for client-side logic."
    },
    {
        "question": "Which module is used to manage ServiceNow tables?",
        "options": [
            "A. System Definition > Tables",
            "B. System Definition > Table Manager",
            "C. System Definition > Schema",
            "D. System Definition > Table Editor"
        ],
        "answer": "A. System Definition > Tables",
        "explanation": "The System Definition > Tables module is used to manage tables."
    },
    {
        "question": "What is the purpose of the 'sys_data_policy' table?",
        "options": [
            "A. To store Data Policies",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store Data Policies",
        "explanation": "The sys_data_policy table stores Data Policies for enforcing field rules."
    },
    {
        "question": "Which feature allows you to create a custom notification template?",
        "options": [
            "A. Notification Template Editor",
            "B. Notification Designer",
            "C. Email Template",
            "D. Notification Builder"
        ],
        "answer": "C. Email Template",
        "explanation": "Email Templates allow creation of custom notification templates."
    },
    {
        "question": "What is the purpose of the 'sys_choice' table?",
        "options": [
            "A. To store choice list values",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store choice list values",
        "explanation": "The sys_choice table stores values for choice lists used in fields."
    },
    {
        "question": "Which module is used to manage ServiceNow reports?",
        "options": [
            "A. Reports > View / Run",
            "B. Reports > Management",
            "C. Reports > Administration",
            "D. Reports > Dashboard"
        ],
        "answer": "A. Reports > View / Run",
        "explanation": "The Reports > View / Run module is used to manage reports."
    },
    {
        "question": "What is the purpose of the 'sys_ui_form' table?",
        "options": [
            "A. To store form layouts",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store form layouts",
        "explanation": "The sys_ui_form table stores custom form layouts."
    },
    {
        "question": "Which feature allows you to create a custom SLA definition?",
        "options": [
            "A. SLA Designer",
            "B. SLA Definition",
            "C. SLA Editor",
            "D. SLA Manager"
        ],
        "answer": "B. SLA Definition",
        "explanation": "The SLA Definition module allows creation of custom SLA definitions."
    },
    {
        "question": "What is the purpose of the 'sys_ui_list' table?",
        "options": [
            "A. To store list layouts",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store list layouts",
        "explanation": "The sys_ui_list table stores custom list layouts."
    },
    {
        "question": "Which module is used to manage ServiceNow dashboards?",
        "options": [
            "A. Dashboards > Homepages",
            "B. Dashboards > Management",
            "C. Dashboards > Administration",
            "D. Dashboards > Overview"
        ],
        "answer": "A. Dashboards > Homepages",
        "explanation": "The Dashboards > Homepages module is used to manage dashboards."
    },
    {
        "question": "What is the purpose of the 'sys_ui_macro' table?",
        "options": [
            "A. To store UI Macros",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store UI Macros",
        "explanation": "The sys_ui_macro table stores UI Macros for custom UI elements."
    },
    {
        "question": "Which feature allows you to create a custom Visual Task Board?",
        "options": [
            "A. Task Board Creator",
            "B. Visual Task Board",
            "C. Task Board Designer",
            "D. Kanban Editor"
        ],
        "answer": "B. Visual Task Board",
        "explanation": "The Visual Task Board feature allows creation of custom task boards."
    },
    {
        "question": "What is the purpose of the 'sys_ui_page' table?",
        "options": [
            "A. To store UI Pages",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store UI Pages",
        "explanation": "The sys_ui_page table stores custom UI Pages."
    },
    {
        "question": "Which module is used to manage ServiceNow events?",
        "options": [
            "A. System Events > Event Log",
            "B. System Events > Management",
            "C. System Events > Registry",
            "D. System Events > Dashboard"
        ],
        "answer": "C. System Events > Registry",
        "explanation": "The System Events > Registry module is used to manage event definitions."
    },
    {
        "question": "What is the purpose of the 'sys_ui_section' table?",
        "options": [
            "A. To store form section layouts",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store form section layouts",
        "explanation": "The sys_ui_section table stores form section layouts."
    },
    {
        "question": "Which feature allows you to create a custom Service Catalog category?",
        "options": [
            "A. Category Creator",
            "B. Service Catalog > Maintain Categories",
            "C. Category Editor",
            "D. Catalog Manager"
        ],
        "answer": "B. Service Catalog > Maintain Categories",
        "explanation": "The Service Catalog > Maintain Categories module allows creation of custom categories."
    },
    {
        "question": "What is the purpose of the 'sys_ui_style' table?",
        "options": [
            "A. To store UI styles",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store UI styles",
        "explanation": "The sys_ui_style table stores UI styles for customizing form appearance."
    },
    {
        "question": "Which module is used to manage ServiceNow scheduled jobs?",
        "options": [
            "A. System Definition > Scheduled Jobs",
            "B. System Definition > Schedules",
            "C. System Definition > Jobs",
            "D. System Definition > Automation"
        ],
        "answer": "A. System Definition > Scheduled Jobs",
        "explanation": "The System Definition > Scheduled Jobs module is used to manage scheduled jobs."
    },
    {
        "question": "What is the purpose of the 'sys_ui_view' table?",
        "options": [
            "A. To store form views",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store form views",
        "explanation": "The sys_ui_view table stores custom form views."
    },
    {
        "question": "Which feature allows you to create a custom import set?",
        "options": [
            "A. Import Set Creator",
            "B. System Import Sets",
            "C. Data Import Manager",
            "D. Import Set Designer"
        ],
        "answer": "B. System Import Sets",
        "explanation": "The System Import Sets module allows creation of custom import sets."
    },
    {
        "question": "What is the purpose of the 'sys_user_grmember' table?",
        "options": [
            "A. To store group memberships",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store group memberships",
        "explanation": "The sys_user_grmember table stores user-group membership assignments."
    },
    {
        "question": "Which module is used to manage ServiceNow UI policies?",
        "options": [
            "A. System UI > UI Policies",
            "B. System UI > Policies",
            "C. System UI > Management",
            "D. System UI > Administration"
        ],
        "answer": "A. System UI > UI Policies",
        "explanation": "The System UI > UI Policies module is used to manage UI policies."
    },
    {
        "question": "What is the purpose of the 'sys_workflow' table?",
        "options": [
            "A. To store workflows",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store workflows",
        "explanation": "The sys_workflow table stores workflow definitions."
    },
    {
        "question": "Which feature allows you to create a custom knowledge base?",
        "options": [
            "A. Knowledge Base Creator",
            "B. Knowledge > Knowledge Bases",
            "C. Knowledge Base Editor",
            "D. Knowledge Manager"
        ],
        "answer": "B. Knowledge > Knowledge Bases",
        "explanation": "The Knowledge > Knowledge Bases module allows creation of custom knowledge bases."
    },
    {
        "question": "What is the purpose of the 'sys_notification' table?",
        "options": [
            "A. To store notification definitions",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store notification definitions",
        "explanation": "The sys_notification table stores notification definitions."
    },
    {
        "question": "Which module is used to manage ServiceNow ACLs?",
        "options": [
            "A. System Security > Access Control (ACL)",
            "B. System Security > Rules",
            "C. System Security > Permissions",
            "D. System Security > Management"
        ],
        "answer": "A. System Security > Access Control (ACL)",
        "explanation": "The System Security > Access Control (ACL) module is used to manage ACLs."
    },
    {
        "question": "What is the purpose of the 'sys_import_set' table?",
        "options": [
            "A. To store import set data",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store import set data",
        "explanation": "The sys_import_set table stores data for import sets."
    },
    {
        "question": "Which feature allows you to create a custom Service Portal page?",
        "options": [
            "A. Page Creator",
            "B. Service Portal Designer",
            "C. Page Editor",
            "D. Portal Manager"
        ],
        "answer": "B. Service Portal Designer",
        "explanation": "The Service Portal Designer allows creation of custom Service Portal pages."
    },
    {
        "question": "What is the purpose of the 'sys_transform_map' table?",
        "options": [
            "A. To store transform map definitions",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store transform map definitions",
        "explanation": "The sys_transform_map table stores transform map definitions for data imports."
    },
    {
        "question": "Which module is used to manage ServiceNow business rules?",
        "options": [
            "A. System Definition > Business Rules",
            "B. System Definition > Rules",
            "C. System Definition > Scripts",
            "D. System Definition > Logic"
        ],
        "answer": "A. System Definition > Business Rules",
        "explanation": "The System Definition > Business Rules module is used to manage business rules."
    },
    {
        "question": "What is the purpose of the 'sys_email_template' table?",
        "options": [
            "A. To store email templates",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store email templates",
        "explanation": "The sys_email_template table stores email templates for notifications."
    },
    {
        "question": "Which feature allows you to create a custom CMDB class?",
        "options": [
            "A. CI Class Manager",
            "B. CMDB Designer",
            "C. CI Editor",
            "D. CMDB Manager"
        ],
        "answer": "A. CI Class Manager",
        "explanation": "The CI Class Manager allows creation of custom CMDB classes."
    },
    {
        "question": "What is the purpose of the 'sys_ui_policy_action' table?",
        "options": [
            "A. To store UI Policy Actions",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store UI Policy Actions",
        "explanation": "The sys_ui_policy_action table stores UI Policy Actions for form field behavior."
    },
    {
        "question": "Which module is used to manage ServiceNow import sets?",
        "options": [
            "A. System Import Sets > Import Sets",
            "B. System Import Sets > Data",
            "C. System Import Sets > Management",
            "D. System Import Sets > Administration"
        ],
        "answer": "A. System Import Sets > Import Sets",
        "explanation": "The System Import Sets > Import Sets module is used to manage import sets."
    },
    {
        "question": "What is the purpose of the 'sys_flow_designer' table?",
        "options": [
            "A. To store Flow Designer flows",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store Flow Designer flows",
        "explanation": "The sys_flow_designer table stores Flow Designer flow definitions."
    },
    {
        "question": "Which feature allows you to create a custom report schedule?",
        "options": [
            "A. Report Scheduler",
            "B. Scheduled Reports",
            "C. Report Automation",
            "D. Report Manager"
        ],
        "answer": "B. Scheduled Reports",
        "explanation": "The Scheduled Reports feature allows creation of custom report schedules."
    },
    {
        "question": "What is the purpose of the 'sys_sp_widget' table?",
        "options": [
            "A. To store Service Portal widgets",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store Service Portal widgets",
        "explanation": "The sys_sp_widget table stores Service Portal widget definitions."
    },
    {
        "question": "Which module is used to manage ServiceNow client scripts?",
        "options": [
            "A. System Definition > Client Scripts",
            "B. System Definition > Scripts",
            "C. System Definition > Client Logic",
            "D. System Definition > Client Management"
        ],
        "answer": "A. System Definition > Client Scripts",
        "explanation": "The System Definition > Client Scripts module is used to manage client scripts."
    },
    {
        "question": "What is the purpose of the 'sys_sp_page' table?",
        "options": [
            "A. To store Service Portal pages",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store Service Portal pages",
        "explanation": "The sys_sp_page table stores Service Portal page definitions."
    },
    {
        "question": "Which feature allows you to create a custom SLA condition?",
        "options": [
            "A. SLA Condition Editor",
            "B. SLA Definition",
            "C. SLA Rule Manager",
            "D. SLA Condition Builder"
        ],
        "answer": "B. SLA Definition",
        "explanation": "The SLA Definition module allows creation of custom SLA conditions."
    },
    {
        "question": "What is the purpose of the 'sys_report' table?",
        "options": [
            "A. To store report definitions",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store report definitions",
        "explanation": "The sys_report table stores report definitions."
    },
    {
        "question": "Which module is used to manage ServiceNow UI actions?",
        "options": [
            "A. System Definition > UI Actions",
            "B. System Definition > Actions",
            "C. System Definition > UI Management",
            "D. System Definition > UI Logic"
        ],
        "answer": "A. System Definition > UI Actions",
        "explanation": "The System Definition > UI Actions module is used to manage UI actions."
    },
    {
        "question": "What is the purpose of the 'sys_sla' table?",
        "options": [
            "A. To store SLA definitions",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store SLA definitions",
        "explanation": "The sys_sla table stores SLA definitions."
    },
    {
        "question": "Which feature allows you to create a custom Service Catalog item?",
        "options": [
            "A. Catalog Item Creator",
            "B. Service Catalog > Maintain Items",
            "C. Catalog Item Editor",
            "D. Catalog Manager"
        ],
        "answer": "B. Service Catalog > Maintain Items",
        "explanation": "The Service Catalog > Maintain Items module allows creation of custom catalog items."
    },
    {
        "question": "What is the purpose of the 'sys_update_set' table?",
        "options": [
            "A. To store Update Set definitions",
            "B. To manage user roles",
            "C. To track system events",
            "D. To store audit logs"
        ],
        "answer": "A. To store Update Set definitions",
        "explanation": "The sys_update_set table stores Update Set definitions."
    }
]