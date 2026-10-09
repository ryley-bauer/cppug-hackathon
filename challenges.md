---
layout: page
title: Challenges
permalink: /challenges/
description: The seven prepared challenges for the CPPUG Power Platform Hackathon, with a scenario, users, a starter build, stretch ideas, and suggested data for each.
hide_title: true
---

<section class="site-section">
    <h2>Pick a Challenge</h2>
    <p style="text-align: center;">Each challenge fits a four-hour build. Build the starter version first and add stretch ideas only when it works. Prefer your own idea? Choose Open Build. <a href="{{ site.pack_pdf | relative_url }}">Printable version: pages 4 and 5 of the Participant Pack (PDF)</a>.</p>
    <div class="pack-grid">
        {% for c in site.data.challenges %}
        <div class="pack-card c{{ forloop.index0 | modulo: 6 }}">
            <h3>{{ forloop.index }}. {{ c.name }}</h3>
            <dl>
                <dt>Scenario</dt><dd>{{ c.scenario }}</dd>
                <dt>Users</dt><dd>{{ c.users }}</dd>
                <dt>Starter build (MVP)</dt><dd>{{ c.starter }}</dd>
                <dt>Stretch ideas</dt><dd>{{ c.stretch }}</dd>
                <dt>Suggested data</dt><dd>{{ c.data }}</dd>
                <dt>Likely tools</dt><dd>{{ c.tools }}</dd>
            </dl>
        </div>
        {% endfor %}
    </div>
    <p><strong>Tip.</strong> Start with sample data. Ten realistic rows make a better demo than an empty app. AI tools, Microsoft Learn, and search are all allowed. Tell the judges what you used.</p>
</section>
