import pandas as pd

month_dct = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

string = ""
last_year = "Nothingset"

df = pd.read_csv("talks.csv")
df = df.iloc[0:36]
for index, row in df[::-1].iterrows():
    year = int(row["Year"])
    month = month_dct[row["Month"]]
    title = row["Title"]
    if not isinstance(title, str):
        title = ""
    event = row["Event"]
    if not isinstance(event, str):
        event = ""

    # Invitationtag
    invitedBy = row["Invited by"]
    invitationTag = ""

    if isinstance(invitedBy, str):
        invitationTag = f"<span>Invited by {invitedBy}</span>"

    # Locationtag
    online = row["Participation"] == "Online"
    university = row["University"]
    city = row["City"]
    state = row["Country"]
    typus = row["Event Type"]
    marker = '<i class="fa-solid fa-map-pin"></i>'
    if university and isinstance(university, str):  # Make shure a university is given
        locationTagRaw = f"{university}, {city}, {state}"
    else:
        locationTagRaw = f"{city}, {state}"

    if online and typus == "Seminar":
        event = event + f" ({locationTagRaw})"
        locationTag = f"<span>Online</span>"
    elif online:
        locationTag = f"<span>Online ({locationTagRaw})</span>"
    else:
        event = event
        locationTag = f"<span>{marker} {locationTagRaw}</span>"

    # Institution tag
    institution = row["Institution"]
    institutionTag = ""
    if institution and isinstance(institution, str):
        institutionTag = f"<span>{institution}</span>"

    # Typetag
    typus = row["Event Type"]
    typeTag = f"<span>{typus}</span>"

    # Year grouping
    if last_year!=year:
        # If already stuff was written the tag has to be closed.
        if last_year!="Nothingset":
            string += f"""
                    </div>
                </section>
"""
        last_year = year
        # Open a new tag.
        string += f"""
                <section class="talk-year-group">
                    <h3 class="talk-year">{year}</h3>
                    <div class="talk-list">             
"""




    string += f"""                        
                        
                        <article class="talk-item">
                            <p class="talk-date">{month}</p>
                            <div class="talk-details">
                                <h3 class="talk-title">
                                    {title}
                                </h3>
                                <p class="talk-event">
                                    {event}
                                </p>
                                <div class="talk-tags">
                                    {invitationTag}
                                    {institutionTag}
                                    {locationTag}
                                    {typeTag}
                                </div>
                            </div>
                        </article>
    """


string += """
                    </div>
                </section>
"""

with open("talks.txt", "w", encoding="utf-8") as f:
    f.write(string)