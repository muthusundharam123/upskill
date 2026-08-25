
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
