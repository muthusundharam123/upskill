from pathlib import Path
import json
from flask import Flask, render_template, jsonify


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
DATA_DIR = BASE_DIR / "data"


# ============================================================
# CREATE DIRECTORIES
# ============================================================

TEMPLATES_DIR.mkdir(exist_ok=True)
STATIC_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)


# ============================================================
# JSON ROADMAP DATA
# ============================================================

ROADMAP = [

    {
        "id": "frontend",
        "order": 1,
        "title": "Frontend Fundamentals",
        "icon": "🎨",
        "description": "Build strong browser and UI fundamentals.",
        "topics": [

            {
                "id": "html",
                "name": "HTML5",
                "level": "Essential"
            },

            {
                "id": "css",
                "name": "CSS3",
                "level": "Essential"
            },

            {
                "id": "responsive",
                "name": "Responsive Design",
                "level": "Essential"
            },

            {
                "id": "browser",
                "name": "Browser DevTools",
                "level": "Important"
            },

            {
                "id": "accessibility",
                "name": "Web Accessibility",
                "level": "Useful"
            }

        ]
    },


    {
        "id": "javascript",
        "order": 2,
        "title": "JavaScript",
        "icon": "🟨",
        "description": "Master JavaScript before depending heavily on frameworks.",
        "topics": [

            {
                "id": "variables",
                "name": "Variables, Scope & Hoisting",
                "level": "Essential"
            },

            {
                "id": "functions",
                "name": "Functions",
                "level": "Essential"
            },

            {
                "id": "objects",
                "name": "Objects & Prototypes",
                "level": "Essential"
            },

            {
                "id": "arrays",
                "name": "Arrays & Array Methods",
                "level": "Essential"
            },

            {
                "id": "promises",
                "name": "Promises & Async/Await",
                "level": "Essential"
            },

            {
                "id": "eventloop",
                "name": "Event Loop",
                "level": "Important"
            },

            {
                "id": "dom",
                "name": "DOM Manipulation",
                "level": "Essential"
            },

            {
                "id": "fetch",
                "name": "Fetch API",
                "level": "Important"
            }

        ]
    },


    {
        "id": "jquery",
        "order": 3,
        "title": "jQuery",
        "icon": "⚡",
        "description": "Understand legacy enterprise applications.",
        "topics": [

            {
                "id": "selectors",
                "name": "Selectors",
                "level": "Essential"
            },

            {
                "id": "events",
                "name": "Events",
                "level": "Essential"
            },

            {
                "id": "ajax",
                "name": "AJAX",
                "level": "Important"
            },

            {
                "id": "dom",
                "name": "DOM Manipulation",
                "level": "Important"
            }

        ]
    },


    {
        "id": "typescript",
        "order": 4,
        "title": "TypeScript",
        "icon": "🔷",
        "description": "Modern typed JavaScript.",
        "topics": [

            {
                "id": "types",
                "name": "Types",
                "level": "Essential"
            },

            {
                "id": "interfaces",
                "name": "Interfaces",
                "level": "Essential"
            },

            {
                "id": "generics",
                "name": "Generics",
                "level": "Important"
            },

            {
                "id": "decorators",
                "name": "Decorators",
                "level": "Useful"
            },

            {
                "id": "advanced",
                "name": "Advanced TypeScript",
                "level": "Important"
            }

        ]
    },


    {
        "id": "angular",
        "order": 5,
        "title": "Angular",
        "icon": "🅰️",
        "description": "Become strong in modern Angular development.",
        "topics": [

            {
                "id": "components",
                "name": "Components",
                "level": "Essential"
            },

            {
                "id": "templates",
                "name": "Templates & Directives",
                "level": "Essential"
            },

            {
                "id": "services",
                "name": "Services & Dependency Injection",
                "level": "Essential"
            },

            {
                "id": "routing",
                "name": "Routing",
                "level": "Essential"
            },

            {
                "id": "forms",
                "name": "Reactive Forms",
                "level": "Essential"
            },

            {
                "id": "http",
                "name": "HttpClient",
                "level": "Essential"
            },

            {
                "id": "rxjs",
                "name": "RxJS",
                "level": "Essential"
            },

            {
                "id": "state",
                "name": "State Management",
                "level": "Important"
            },

            {
                "id": "lazy",
                "name": "Lazy Loading",
                "level": "Important"
            },

            {
                "id": "performance",
                "name": "Angular Performance",
                "level": "Important"
            }

        ]
    },


    {
        "id": "csharp",
        "order": 6,
        "title": "C#",
        "icon": "🔵",
        "description": "Deep C# knowledge for senior .NET roles.",
        "topics": [

            {
                "id": "oop",
                "name": "OOP",
                "level": "Essential"
            },

            {
                "id": "collections",
                "name": "Collections",
                "level": "Essential"
            },

            {
                "id": "generics",
                "name": "Generics",
                "level": "Essential"
            },

            {
                "id": "delegates",
                "name": "Delegates & Events",
                "level": "Important"
            },

            {
                "id": "linq",
                "name": "LINQ",
                "level": "Essential"
            },

            {
                "id": "async",
                "name": "Async/Await",
                "level": "Essential"
            },

            {
                "id": "threads",
                "name": "Threading",
                "level": "Important"
            },

            {
                "id": "memory",
                "name": "Memory Management & GC",
                "level": "Important"
            },

            {
                "id": "reflection",
                "name": "Reflection",
                "level": "Useful"
            },

            {
                "id": "solid",
                "name": "SOLID Principles",
                "level": "Essential"
            }

        ]
    },


    {
        "id": "aspnet",
        "order": 7,
        "title": "ASP.NET Core",
        "icon": "🌐",
        "description": "Build production-grade .NET applications.",
        "topics": [

            {
                "id": "mvc",
                "name": "MVC Architecture",
                "level": "Essential"
            },

            {
                "id": "webapi",
                "name": "REST APIs",
                "level": "Essential"
            },

            {
                "id": "middleware",
                "name": "Middleware",
                "level": "Essential"
            },

            {
                "id": "di",
                "name": "Dependency Injection",
                "level": "Essential"
            },

            {
                "id": "configuration",
                "name": "Configuration & Options",
                "level": "Important"
            },

            {
                "id": "authentication",
                "name": "Authentication & Authorization",
                "level": "Essential"
            },

            {
                "id": "jwt",
                "name": "JWT",
                "level": "Essential"
            },

            {
                "id": "logging",
                "name": "Logging",
                "level": "Important"
            },

            {
                "id": "caching",
                "name": "Caching",
                "level": "Important"
            },

            {
                "id": "testing",
                "name": "Unit & Integration Testing",
                "level": "Important"
            }

        ]
    },


    {
        "id": "database",
        "order": 8,
        "title": "Database",
        "icon": "🗄️",
        "description": "Become strong in SQL and database design.",
        "topics": [

            {
                "id": "sql",
                "name": "SQL Fundamentals",
                "level": "Essential"
            },

            {
                "id": "joins",
                "name": "Joins",
                "level": "Essential"
            },

            {
                "id": "indexes",
                "name": "Indexes",
                "level": "Essential"
            },

            {
                "id": "transactions",
                "name": "Transactions",
                "level": "Essential"
            },

            {
                "id": "procedures",
                "name": "Stored Procedures",
                "level": "Important"
            },

            {
                "id": "optimization",
                "name": "Query Optimization",
                "level": "Essential"
            },

            {
                "id": "normalization",
                "name": "Normalization",
                "level": "Important"
            },

            {
                "id": "postgresql",
                "name": "PostgreSQL",
                "level": "Important"
            }

        ]
    },


    {
        "id": "dsa",
        "order": 9,
        "title": "DSA",
        "icon": "🧠",
        "description": "Interview-level problem solving.",
        "topics": [

            {
                "id": "complexity",
                "name": "Big O Complexity",
                "level": "Essential"
            },

            {
                "id": "arrays",
                "name": "Arrays",
                "level": "Essential"
            },

            {
                "id": "strings",
                "name": "Strings",
                "level": "Essential"
            },

            {
                "id": "hashing",
                "name": "Hash Tables",
                "level": "Essential"
            },

            {
                "id": "linkedlist",
                "name": "Linked Lists",
                "level": "Essential"
            },

            {
                "id": "stack",
                "name": "Stacks",
                "level": "Essential"
            },

            {
                "id": "queue",
                "name": "Queues",
                "level": "Essential"
            },

            {
                "id": "tree",
                "name": "Trees",
                "level": "Essential"
            },

            {
                "id": "graph",
                "name": "Graphs",
                "level": "Important"
            },

            {
                "id": "heap",
                "name": "Heap / Priority Queue",
                "level": "Important"
            },

            {
                "id": "binarysearch",
                "name": "Binary Search",
                "level": "Essential"
            },

            {
                "id": "recursion",
                "name": "Recursion",
                "level": "Essential"
            },

            {
                "id": "dp",
                "name": "Dynamic Programming",
                "level": "Important"
            },

            {
                "id": "backtracking",
                "name": "Backtracking",
                "level": "Important"
            }

        ]
    },


    {
        "id": "architecture",
        "order": 10,
        "title": "Software Architecture",
        "icon": "🏗️",
        "description": "Think like a senior engineer.",
        "topics": [

            {
                "id": "solid",
                "name": "SOLID",
                "level": "Essential"
            },

            {
                "id": "clean",
                "name": "Clean Architecture",
                "level": "Essential"
            },

            {
                "id": "patterns",
                "name": "Design Patterns",
                "level": "Essential"
            },

            {
                "id": "ddd",
                "name": "Domain Driven Design",
                "level": "Important"
            },

            {
                "id": "cqrs",
                "name": "CQRS",
                "level": "Important"
            },

            {
                "id": "eventdriven",
                "name": "Event Driven Architecture",
                "level": "Important"
            }

        ]
    },


    {
        "id": "systemdesign",
        "order": 11,
        "title": "System Design",
        "icon": "📐",
        "description": "Design systems that scale.",
        "topics": [

            {
                "id": "requirements",
                "name": "Requirement Analysis",
                "level": "Essential"
            },

            {
                "id": "api",
                "name": "API Design",
                "level": "Essential"
            },

            {
                "id": "scaling",
                "name": "Horizontal & Vertical Scaling",
                "level": "Essential"
            },

            {
                "id": "loadbalancer",
                "name": "Load Balancers",
                "level": "Essential"
            },

            {
                "id": "cache",
                "name": "Caching",
                "level": "Essential"
            },

            {
                "id": "queue",
                "name": "Message Queues",
                "level": "Essential"
            },

            {
                "id": "database",
                "name": "Database Scaling",
                "level": "Important"
            },

            {
                "id": "microservices",
                "name": "Microservices",
                "level": "Essential"
            },

            {
                "id": "observability",
                "name": "Observability",
                "level": "Important"
            }

        ]
    },


    {
        "id": "distributed",
        "order": 12,
        "title": "Distributed Systems",
        "icon": "🌍",
        "description": "Understand systems beyond one server.",
        "topics": [

            {
                "id": "consistency",
                "name": "Consistency",
                "level": "Important"
            },

            {
                "id": "availability",
                "name": "Availability",
                "level": "Important"
            },

            {
                "id": "partition",
                "name": "Network Partition",
                "level": "Important"
            },

            {
                "id": "cap",
                "name": "CAP Theorem",
                "level": "Essential"
            },

            {
                "id": "idempotency",
                "name": "Idempotency",
                "level": "Essential"
            },

            {
                "id": "distributedcache",
                "name": "Distributed Cache",
                "level": "Important"
            }

        ]
    },


    {
        "id": "devops",
        "order": 13,
        "title": "DevOps",
        "icon": "⚙️",
        "description": "Deploy and operate production applications.",
        "topics": [

            {
                "id": "git",
                "name": "Git",
                "level": "Essential"
            },

            {
                "id": "linux",
                "name": "Linux",
                "level": "Essential"
            },

            {
                "id": "docker",
                "name": "Docker",
                "level": "Essential"
            },

            {
                "id": "nginx",
                "name": "Nginx",
                "level": "Important"
            },

            {
                "id": "cicd",
                "name": "CI/CD",
                "level": "Essential"
            },

            {
                "id": "monitoring",
                "name": "Monitoring",
                "level": "Important"
            },

            {
                "id": "logging",
                "name": "Centralized Logging",
                "level": "Important"
            }

        ]
    },


    {
        "id": "cloud",
        "order": 14,
        "title": "Cloud",
        "icon": "☁️",
        "description": "Cloud skills for modern backend engineers.",
        "topics": [

            {
                "id": "azure",
                "name": "Azure Fundamentals",
                "level": "Essential"
            },

            {
                "id": "appservice",
                "name": "Azure App Service",
                "level": "Important"
            },

            {
                "id": "storage",
                "name": "Cloud Storage",
                "level": "Important"
            },

            {
                "id": "database",
                "name": "Cloud Databases",
                "level": "Important"
            },

            {
                "id": "functions",
                "name": "Serverless Functions",
                "level": "Useful"
            },

            {
                "id": "kubernetes",
                "name": "Kubernetes",
                "level": "Important"
            }

        ]
    },


    {
        "id": "ai",
        "order": 15,
        "title": "AI for Developers",
        "icon": "🤖",
        "description": "Use AI as an engineering multiplier.",
        "topics": [

            {
                "id": "python",
                "name": "Python Basics",
                "level": "Useful"
            },

            {
                "id": "mlbasics",
                "name": "Machine Learning Fundamentals",
                "level": "Useful"
            },

            {
                "id": "llm",
                "name": "LLM Fundamentals",
                "level": "Important"
            },

            {
                "id": "prompt",
                "name": "Prompt Engineering",
                "level": "Important"
            },

            {
                "id": "rag",
                "name": "RAG",
                "level": "Important"
            },

            {
                "id": "embeddings",
                "name": "Embeddings & Vector Databases",
                "level": "Important"
            },

            {
                "id": "agents",
                "name": "AI Agents",
                "level": "Useful"
            }

        ]
    },


    {
        "id": "interview",
        "order": 16,
        "title": "Interview Preparation",
        "icon": "🎯",
        "description": "Convert knowledge into offers.",
        "topics": [

            {
                "id": "coding",
                "name": "Coding Problems",
                "level": "Essential"
            },

            {
                "id": "csharpquestions",
                "name": "C# Interview Questions",
                "level": "Essential"
            },

            {
                "id": "dotnetquestions",
                "name": ".NET Interview Questions",
                "level": "Essential"
            },

            {
                "id": "sqlquestions",
                "name": "SQL Interview Questions",
                "level": "Essential"
            },

            {
                "id": "angularquestions",
                "name": "Angular Interview Questions",
                "level": "Essential"
            },

            {
                "id": "systemdesignquestions",
                "name": "System Design Interviews",
                "level": "Essential"
            },

            {
                "id": "project",
                "name": "Project Deep Dive",
                "level": "Essential"
            },

            {
                "id": "behavioral",
                "name": "Behavioral Questions",
                "level": "Important"
            }

        ]
    }

]


# ============================================================
# CREATE JSON FILES
# ============================================================

def create_json_files():

    for section in ROADMAP:

        file_path = DATA_DIR / f"{section['id']}.json"

        # Don't overwrite existing files.
        # This is important because you will edit them later.
        if not file_path.exists():

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    section,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            print(
                f"Created: data/{section['id']}.json"
            )

        else:

            print(
                f"Exists : data/{section['id']}.json"
            )


# ============================================================
# HTML
# ============================================================

INDEX_HTML = r'''
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>DevPath | Roadmap</title>

<link rel="stylesheet"
      href="{{ url_for('static', filename='style.css') }}">

</head>

<body>


<header class="header">

    <div class="brand">

        <div class="brand-icon">
            🚀
        </div>

        <div>

            <h1>DevPath</h1>

            <span>
                Dot Net Developer Roadmap
            </span>

        </div>

    </div>


    <div class="header-stats">

        <div class="stat">

            <strong id="completedCount">
                0
            </strong>

            <span>
                Completed
            </span>

        </div>


        <div class="stat">

            <strong id="totalCount">
                0
            </strong>

            <span>
                Total Topics
            </span>

        </div>


        <div class="progress-box">

            <div class="progress-label">

                <span>
                    Overall Progress
                </span>

                <strong id="progressPercent">
                    0%
                </strong>

            </div>


            <div class="progress">

                <div id="progressBar"></div>

            </div>

        </div>

    </div>

</header>



<div class="layout">


    <aside class="sidebar">

        <div class="sidebar-title">
            ROADMAP
        </div>

        <div id="sidebar"></div>

    </aside>



    <main class="main">


        <section class="hero">

            <div>

                <div class="eyebrow">
                    FULL STACK → SENIOR → Dream
                </div>

                <h2>

                    Build your path.

                    <span>
                        Master the fundamentals.
                    </span>

                </h2>

                <p>

                    Track C#, .NET, Angular, SQL,
                    DSA, System Design, Cloud,
                    DevOps and AI from one place.

                </p>

            </div>


            <div class="hero-progress">

                <div class="circle">

                    <span id="circlePercent">
                        0%
                    </span>

                </div>

            </div>

        </section>



        <div class="toolbar">


            <div class="search">

                🔎

                <input
                    id="searchInput"
                    type="text"
                    placeholder="Search topics...">

            </div>


            <div class="filters">

                <button
                    class="filter active"
                    data-filter="all">

                    All

                </button>


                <button
                    class="filter"
                    data-filter="Essential">

                    Essential

                </button>


                <button
                    class="filter"
                    data-filter="Important">

                    Important

                </button>


                <button
                    class="filter"
                    data-filter="Useful">

                    Useful

                </button>

            </div>

        </div>



        <div id="roadmap"></div>


    </main>

</div>



<script src="{{ url_for('static', filename='app.js') }}"></script>

</body>

</html>
'''


# ============================================================
# WRITE HTML
# ============================================================

def create_html():

    file_path = TEMPLATES_DIR / "index.html"

    if not file_path.exists():

        file_path.write_text(
            INDEX_HTML,
            encoding="utf-8"
        )

        print(
            "Created: index.html"
        )

    else:

        print(
            "Exists : index.html"
        )


# ============================================================
# CSS
# ============================================================

STYLE_CSS = r'''
* {
    box-sizing: border-box;
}


body {
    margin: 0;

    font-family:
        Inter,
        Segoe UI,
        Arial,
        sans-serif;

    background: #f5f7fb;

    color: #172033;
}


.header {

    height: 82px;

    background: rgba(255,255,255,.94);

    border-bottom: 1px solid #e5e8ef;

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 0 32px;

    position: sticky;

    top: 0;

    z-index: 100;

    backdrop-filter: blur(14px);
}


.brand {

    display: flex;

    align-items: center;

    gap: 13px;
}


.brand-icon {

    width: 44px;

    height: 44px;

    border-radius: 13px;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 22px;

    background: #111827;

    color: white;
}


.brand h1 {

    margin: 0;

    font-size: 21px;

}


.brand span {

    font-size: 12px;

    color: #7b8495;
}


.header-stats {

    display: flex;

    align-items: center;

    gap: 28px;
}


.stat {

    display: flex;

    flex-direction: column;

    gap: 2px;
}


.stat strong {

    font-size: 18px;
}


.stat span {

    font-size: 11px;

    color: #8a93a4;
}


.progress-box {

    width: 170px;
}


.progress-label {

    display: flex;

    justify-content: space-between;

    font-size: 11px;

    margin-bottom: 7px;
}


.progress {

    height: 7px;

    background: #e8ebf1;

    border-radius: 20px;

    overflow: hidden;
}


#progressBar {

    width: 0%;

    height: 100%;

    background: #111827;

    transition: width .4s;
}


.layout {

    display: flex;

    min-height: calc(100vh - 82px);
}


.sidebar {

    width: 250px;

    background: white;

    border-right: 1px solid #e5e8ef;

    padding: 28px 18px;

    position: sticky;

    top: 82px;

    height: calc(100vh - 82px);

    overflow-y: auto;
}


.sidebar-title {

    font-size: 10px;

    font-weight: 700;

    letter-spacing: 1.5px;

    color: #9aa2b1;

    padding: 0 12px 15px;
}


.sidebar-item {

    width: 100%;

    border: 0;

    background: transparent;

    padding: 11px 12px;

    border-radius: 9px;

    display: flex;

    align-items: center;

    gap: 10px;

    cursor: pointer;

    text-align: left;

    color: #596273;

    margin-bottom: 3px;
}


.sidebar-item:hover {

    background: #f4f6f9;

    color: #111827;
}


.sidebar-icon {

    width: 26px;

    text-align: center;
}


.sidebar-name {

    font-size: 13px;

    font-weight: 600;
}


.main {

    flex: 1;

    max-width: 1400px;

    padding: 36px 42px;
}


.hero {

    background: #111827;

    border-radius: 22px;

    padding: 40px;

    color: white;

    display: flex;

    align-items: center;

    justify-content: space-between;

    margin-bottom: 28px;
}


.eyebrow {

    font-size: 10px;

    letter-spacing: 2px;

    color: #aeb7c8;

    margin-bottom: 13px;
}


.hero h2 {

    margin: 0;

    font-size: 34px;
}


.hero h2 span {

    color: #9ca8bb;
}


.hero p {

    color: #aeb7c8;

    max-width: 600px;

    line-height: 1.6;

    font-size: 14px;
}


.circle {

    width: 110px;

    height: 110px;

    border-radius: 50%;

    border: 7px solid #343d4d;

    display: flex;

    align-items: center;

    justify-content: center;
}


.circle span {

    font-size: 22px;

    font-weight: 700;
}


.toolbar {

    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-bottom: 25px;
}


.search {

    background: white;

    border: 1px solid #e4e7ed;

    border-radius: 10px;

    height: 42px;

    display: flex;

    align-items: center;

    padding: 0 14px;

    width: 320px;

    gap: 9px;
}


.search input {

    border: 0;

    outline: 0;

    width: 100%;

    font-size: 13px;
}


.filters {

    display: flex;

    gap: 7px;
}


.filter {

    border: 1px solid #e2e5eb;

    background: white;

    border-radius: 8px;

    padding: 8px 13px;

    cursor: pointer;

    font-size: 12px;
}


.filter.active {

    background: #111827;

    border-color: #111827;

    color: white;
}


.section {

    background: white;

    border: 1px solid #e6e9ef;

    border-radius: 16px;

    margin-bottom: 18px;

    overflow: hidden;
}


.section-header {

    padding: 21px 24px;

    border-bottom: 1px solid #edf0f4;

    display: flex;

    align-items: center;

    justify-content: space-between;
}


.section-title {

    display: flex;

    align-items: center;

    gap: 13px;
}


.section-icon {

    width: 42px;

    height: 42px;

    background: #f3f5f8;

    border-radius: 11px;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 21px;
}


.section-title h3 {

    margin: 0;

    font-size: 17px;
}


.section-title p {

    margin: 4px 0 0;

    color: #8a93a4;

    font-size: 11px;
}


.section-progress {

    text-align: right;
}


.section-progress strong {

    font-size: 14px;
}


.section-progress span {

    display: block;

    font-size: 10px;

    color: #929aaa;
}


.topics {

    padding: 10px 24px 20px;
}


.topic {

    display: flex;

    align-items: center;

    gap: 14px;

    padding: 13px 10px;

    border-bottom: 1px solid #f0f2f5;
}


.checkbox {

    width: 19px;

    height: 19px;

    border: 1.5px solid #cbd1da;

    border-radius: 6px;

    cursor: pointer;

    display: flex;

    align-items: center;

    justify-content: center;

    flex-shrink: 0;
}


.checkbox.completed {

    background: #111827;

    border-color: #111827;

    color: white;
}


.topic-name {

    flex: 1;

    font-size: 13px;

    font-weight: 600;
}


.topic.completed .topic-name {

    text-decoration: line-through;

    color: #9aa1ad;
}


.level {

    font-size: 9px;

    padding: 4px 8px;

    border-radius: 20px;

    background: #f0f2f5;

    color: #697386;

    font-weight: 700;
}


@media(max-width:900px) {

    .header-stats {
        display:none;
    }

    .sidebar {
        display:none;
    }

    .main {
        padding:20px;
    }

    .hero {
        padding:28px;

        flex-direction:column;

        align-items:flex-start;
    }

    .toolbar {
        flex-direction:column;

        align-items:stretch;
    }

    .search {
        width:100%;
    }

}
'''


def create_css():

    file_path = STATIC_DIR / "style.css"

    if not file_path.exists():

        file_path.write_text(
            STYLE_CSS,
            encoding="utf-8"
        )

        print(
            "Created: static/style.css"
        )

    else:

        print(
            "Exists : static/style.css"
        )


# ============================================================
# JAVASCRIPT
# ============================================================

APP_JS = r'''
let roadmap = [];

let completed =
    JSON.parse(
        localStorage.getItem(
            "devpath_completed"
        ) || "{}"
    );


let currentFilter = "all";


document.addEventListener(
    "DOMContentLoaded",
    loadRoadmap
);


async function loadRoadmap() {

    const response =
        await fetch("/api/roadmap");

    roadmap =
        await response.json();

    roadmap.sort(
        (a,b) =>
            (a.order || 999) -
            (b.order || 999)
    );

    renderSidebar();

    renderRoadmap();

    updateProgress();
}


function renderSidebar() {

    const sidebar =
        document.getElementById(
            "sidebar"
        );

    sidebar.innerHTML = "";


    roadmap.forEach(section => {

        const button =
            document.createElement(
                "button"
            );


        button.className =
            "sidebar-item";


        button.innerHTML = `

            <span class="sidebar-icon">
                ${section.icon || "📘"}
            </span>

            <span class="sidebar-name">
                ${section.title}
            </span>

        `;


        button.onclick = () => {

            const element =
                document.getElementById(
                    `section-${section.id}`
                );


            if (element) {

                element.scrollIntoView({
                    behavior: "smooth"
                });

            }

        };


        sidebar.appendChild(button);

    });

}


function renderRoadmap() {

    const container =
        document.getElementById(
            "roadmap"
        );


    container.innerHTML = "";


    const search =
        document
        .getElementById(
            "searchInput"
        )
        .value
        .toLowerCase();


    roadmap.forEach(section => {

        let topics =
            section.topics || [];


        topics =
            topics.filter(topic => {

                const searchMatch =
                    topic.name
                    .toLowerCase()
                    .includes(search);


                const filterMatch =
                    currentFilter === "all" ||
                    topic.level === currentFilter;


                return (
                    searchMatch &&
                    filterMatch
                );

            });


        if (!topics.length) {
            return;
        }


        const sectionElement =
            document.createElement(
                "section"
            );


        sectionElement.className =
            "section";


        sectionElement.id =
            `section-${section.id}`;


        const done =
            section.topics.filter(
                topic =>
                    completed[
                        `${section.id}_${topic.id}`
                    ]
            ).length;


        sectionElement.innerHTML = `

            <div class="section-header">

                <div class="section-title">

                    <div class="section-icon">
                        ${section.icon || "📘"}
                    </div>

                    <div>

                        <h3>
                            ${section.title}
                        </h3>

                        <p>
                            ${section.description || ""}
                        </p>

                    </div>

                </div>


                <div class="section-progress">

                    <strong>
                        ${done}/${section.topics.length}
                    </strong>

                    <span>
                        completed
                    </span>

                </div>

            </div>


            <div class="topics"></div>

        `;


        const topicsContainer =
            sectionElement.querySelector(
                ".topics"
            );


        topics.forEach(topic => {

            const key =
                `${section.id}_${topic.id}`;


            const isCompleted =
                !!completed[key];


            const element =
                document.createElement(
                    "div"
                );


            element.className =
                "topic" +
                (isCompleted
                    ? " completed"
                    : "");


            element.innerHTML = `

                <div class="checkbox ${
                    isCompleted
                        ? "completed"
                        : ""
                }">

                    ${
                        isCompleted
                            ? "✓"
                            : ""
                    }

                </div>


                <div class="topic-name">

                    ${topic.name}

                </div>


                <div class="level">

                    ${topic.level}

                </div>

            `;


            element
                .querySelector(
                    ".checkbox"
                )
                .onclick = () => {

                    completed[key] =
                        !completed[key];


                    localStorage.setItem(
                        "devpath_completed",
                        JSON.stringify(
                            completed
                        )
                    );


                    renderRoadmap();

                    updateProgress();

                };


            topicsContainer.appendChild(
                element
            );

        });


        container.appendChild(
            sectionElement
        );

    });

}


function updateProgress() {

    let total = 0;

    let done = 0;


    roadmap.forEach(section => {

        section.topics.forEach(topic => {

            total++;


            if (
                completed[
                    `${section.id}_${topic.id}`
                ]
            ) {

                done++;

            }

        });

    });


    const percentage =
        total
            ? Math.round(
                done / total * 100
            )
            : 0;


    document.getElementById(
        "completedCount"
    ).textContent = done;


    document.getElementById(
        "totalCount"
    ).textContent = total;


    document.getElementById(
        "progressPercent"
    ).textContent =
        `${percentage}%`;


    document.getElementById(
        "progressBar"
    ).style.width =
        `${percentage}%`;


    document.getElementById(
        "circlePercent"
    ).textContent =
        `${percentage}%`;

}


document
.getElementById(
    "searchInput"
)
.addEventListener(
    "input",
    renderRoadmap
);


document
.querySelectorAll(
    ".filter"
)
.forEach(button => {

    button.onclick = () => {

        document
        .querySelectorAll(
            ".filter"
        )
        .forEach(
            b =>
            b.classList.remove(
                "active"
            )
        );


        button.classList.add(
            "active"
        );


        currentFilter =
            button.dataset.filter;


        renderRoadmap();

    };

});
'''


def create_js():

    file_path = STATIC_DIR / "app.js"

    if not file_path.exists():

        file_path.write_text(
            APP_JS,
            encoding="utf-8"
        )

        print(
            "Created: static/app.js"
        )

    else:

        print(
            "Exists : static/app.js"
        )


# ============================================================
# FLASK
# ============================================================

app = Flask(__name__)


@app.route("/")
def index():

    return render_template(
        "index.html"
    )


@app.route("/api/roadmap")
def api_roadmap():

    sections = []


    for file in DATA_DIR.glob("*.json"):

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                sections.append(
                    json.load(f)
                )

        except Exception as error:

            print(
                f"Error reading {file}: {error}"
            )


    sections.sort(
        key=lambda x:
        x.get("order", 999)
    )


    return jsonify(sections)


# ============================================================
# SETUP
# ============================================================

def setup():

    print()
    print("=" * 55)
    print(" DevPath - Project Setup")
    print("=" * 55)
    print()


    print(
        f"Project directory: {BASE_DIR}"
    )

    print()


    create_json_files()

    print()

    create_html()

    create_css()

    create_js()

    print()

    print("=" * 55)

    print(" Setup completed!")

    print("=" * 55)

    print()

    print(
        "Open: http://127.0.0.1:5000"
    )

    print()


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    setup()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )