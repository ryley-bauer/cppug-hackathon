---
layout: home
title: Home
description: Join the CPPUG Power Platform Hackathon at Microsoft Calgary on Saturday, October 10, 2026. Build with Power Apps and Power Automate, get matched with a team, learn from mentors, and win PPCC26 passes. RSVP on Meetup.
hero:
  title: "CPPUG Power Platform Hackathon"
  subtitle: "Saturday, October 10, 2026  ·  9:00 AM to 4:00 PM  ·  Microsoft Calgary"
  buttons:
    - text: "RSVP on Meetup"
      url: "https://www.meetup.com/calgary-power-platform-user-group/events/315727499/"
      external: true
    - text: "Check in"
      url: "https://forms.cloud.microsoft/r/B4kKv3YLdp"
      external: true
      secondary: true
    - text: "Participant pack"
      url: "#participant-pack"
      secondary: true
---

<section id="participant-pack" class="site-section" data-aos="fade-up">
    <h2>Participant Pack</h2>
    <p style="text-align: center;">One document for the whole day. Read page 1 tonight. Each team gets a printed copy on its table tomorrow.</p>
    <p style="text-align: center;"><a href="{{ site.pack_pdf | relative_url }}" class="cta-button"><i class="fas fa-file-pdf"></i> Download the Participant Pack (PDF, 6 pages)</a></p>
    <p style="text-align: center;">Volunteering, mentoring, or judging? Read the <a href="{{ site.team_pdf | relative_url }}">Volunteer and Judge Pack (PDF, 3 pages)</a>: role cards, the judging rubric, and the score sheet.</p>
    <div class="pack-grid">
        {% for part in site.data.pack %}
        <a class="pack-card c{{ forloop.index0 | modulo: 6 }}" href="{{ part.link | relative_url }}" style="text-decoration: none;">
            <h3>{{ part.title }}</h3>
            <p>{{ part.summary }}</p>
            <span class="pack-link">{{ part.pages }}</span>
        </a>
        {% endfor %}
    </div>
</section>

<section id="about" class="site-section" data-aos="fade-up">
    <h2>About the Event</h2>
    
    <p>Join Calgary's premier Microsoft Power Platform hackathon! In one Saturday, you'll collaborate with fellow innovators to build real-world business solutions using cutting-edge low-code tools including Power Apps, Power Automate, Power BI, Power Pages, Copilot Studio, and AI Builder.</p>
    
    <p>Whether you're new to Power Platform or a seasoned pro, this event focuses on hands-on learning, meaningful networking, and demonstrating what's possible when technology meets creativity.</p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 3rem; margin: 3rem 0;">
        <div data-aos="fade-right" data-aos-delay="200">
            <h3 style="color: var(--primary-color); margin-bottom: 1.5rem;">📅 Event Details</h3>
            <div style="background: var(--background-light); padding: 1.5rem; border-radius: var(--border-radius); border-left: 4px solid var(--accent-color);">
                <p style="margin-bottom: 0.75rem;"><strong>📅 Date:</strong> Saturday, October 10, 2026, 9:00 AM to 4:00 PM</p>
                <p style="margin-bottom: 0.75rem;"><strong>📍 Venue:</strong> Microsoft Calgary Office, 8th Floor, 110 9 Ave SW, Calgary, AB</p>
                <p style="margin-bottom: 0.75rem;"><strong>👥 Teams:</strong> 2 to 3 people. No team? We will match you.</p>
                <p style="margin: 0;"><strong>🎟️ Cost:</strong> $5 community contribution, given to charity</p>
            </div>
        </div>

        <div data-aos="fade-left" data-aos-delay="400">
            <h3 style="color: var(--primary-color); margin-bottom: 1.5rem;">🎯 Why Participate?</h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 1rem; padding-left: 0;">🏆 <strong>Win Amazing Prizes:</strong> Two individual Power Platform Community Conference 2026 (PPCC26) passes and Lego Clippy mascots</li>
                <li style="margin-bottom: 1rem; padding-left: 0;">🤝 <strong>Network with Experts:</strong> Connect with Calgary's Power Platform community leaders</li>
                <li style="margin-bottom: 1rem; padding-left: 0;">📚 <strong>Learn by Doing:</strong> Hands-on experience with real business challenges</li>
                <li style="margin-bottom: 1rem; padding-left: 0;">🚀 <strong>Showcase Innovation:</strong> Demonstrate your creativity and technical skills</li>
                <li style="margin-bottom: 1rem; padding-left: 0;">💼 <strong>Career Growth:</strong> Gain valuable experience and industry connections</li>
                <li style="margin: 0; padding-left: 0;">🎯 <strong>Professional Development:</strong> Level up your Power Platform expertise</li>
            </ul>
        </div>
    </div>
    
    <div class="cta" style="text-align: center; margin-top: 3rem;">
        <a href="https://www.meetup.com/calgary-power-platform-user-group/events/315727499/" target="_blank" class="cta-button">
            <i class="fas fa-user-plus"></i> RSVP on Meetup
        </a>
    </div>
</section>


<section id="hackathon-overview" class="site-section" data-aos="fade-up">
    <h2>How the Hackathon Works</h2>
    <p>The CPPUG Hackathon brings together Calgary's brightest minds to tackle real business challenges using Microsoft Power Platform. This isn't just a coding competition, it's a collaborative learning experience where beginners and experts work side-by-side to create solutions that matter.</p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 3rem 0;">
        <div data-aos="fade-up" data-aos-delay="100">
            <h3 style="color: var(--primary-color);">🎯 Your Mission</h3>
            <p>Build innovative solutions that solve real business problems or streamline processes using the full Microsoft Power Platform toolkit. Success means creating functional prototypes that demonstrate clear value and potential impact.</p>
        </div>
        
        <div data-aos="fade-up" data-aos-delay="200">
            <h3 style="color: var(--primary-color);">⏰ Time to Innovate</h3>
            <p>You'll have from 10:00 AM to 1:45 PM to collaborate, design, and build, then a live demo for the judges. It's intense, exciting, and incredibly rewarding.</p>
        </div>
        
        <div data-aos="fade-up" data-aos-delay="300">
            <h3 style="color: var(--primary-color);">🔧 What You'll Build</h3>
            <p>Focus on creating a working Minimum Viable Product (MVP) that showcases your core concept. We're looking for functional solutions that prove the Power Platform's potential. Polish comes later, problem-solving comes first!</p>
        </div>
    </div>

    <div style="margin: 4rem 0;">
        <h3 style="color: var(--primary-color); text-align: center; margin-bottom: 2rem;" data-aos="fade-up">📊 Judging Criteria</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem;">
            <div style="text-align: center; padding: 1rem;" data-aos="zoom-in" data-aos-delay="100">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚙️</div>
                <h4 style="margin: 0.5rem 0; color: var(--accent-color);">Functionality (30%)</h4>
                <p style="margin: 0; font-size: 0.9rem;">Does the solution work as demonstrated?</p>
            </div>
            <div style="text-align: center; padding: 1rem;" data-aos="zoom-in" data-aos-delay="200">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔗</div>
                <h4 style="margin: 0.5rem 0; color: var(--accent-color);">Power Platform Use (35%)</h4>
                <p style="margin: 0; font-size: 0.9rem;">How well did you leverage the platform?</p>
            </div>
            <div style="text-align: center; padding: 1rem;" data-aos="zoom-in" data-aos-delay="300">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎨</div>
                <h4 style="margin: 0.5rem 0; color: var(--accent-color);">Design & UX (25%)</h4>
                <p style="margin: 0; font-size: 0.9rem;">Did you plan it, and is it easy to use?</p>
            </div>
            <div style="text-align: center; padding: 1rem;" data-aos="zoom-in" data-aos-delay="400">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎤</div>
                <h4 style="margin: 0.5rem 0; color: var(--accent-color);">Presentation (10%)</h4>
                <p style="margin: 0; font-size: 0.9rem;">How clearly did you communicate?</p>
            </div>
        </div>
    </div>

    <div style="background: var(--background-light); padding: 2rem; border-radius: var(--border-radius); margin: 3rem 0;" data-aos="fade-up">
        <h3 style="color: var(--primary-color); margin-bottom: 1.5rem; text-align: center;">📋 Essential Guidelines</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
            <ul style="margin: 0; padding-left: 1rem; list-style-type: none;">
                <li style="margin-bottom: 0.75rem;">✅ <strong>Team Size:</strong> 2 to 3 members</li>
                <li style="margin-bottom: 0.75rem;">✅ <strong>Fresh Start:</strong> All development during event</li>
                <li style="margin-bottom: 0.75rem;">✅ <strong>Platform Focus:</strong> Use Microsoft Power Platform</li>
            </ul>
            <ul style="margin: 0; padding-left: 1rem; list-style-type: none;">
                <li style="margin-bottom: 0.75rem;">✅ <strong>MVP Mindset:</strong> Function over polish</li>
                <li style="margin-bottom: 0.75rem;">✅ <strong>Team Formation:</strong> Solo participants matched</li>
                <li style="margin-bottom: 0.75rem;">✅ <strong>Success Focus:</strong> Creativity & business impact</li>
            </ul>
        </div>
    </div>

    <div class="cta" style="text-align: center; margin-top: 2rem;">
        <a href="{{ '/faq/' | relative_url }}" class="cta-button">View Complete Rules & FAQ</a>
    </div>
</section>

<section id="agenda" class="site-section" data-aos="fade-up">
    <h2>Your Day at a Glance</h2>
    <ul>
        <li><strong>9:00 AM, Doors open:</strong> Check in and meet your team.</li>
        <li><strong>9:30 to 9:55 AM, Welcome and challenge briefing:</strong> Rules, prepared challenges, and how judging works.</li>
        <li><strong>10:00 AM, Build time:</strong> Plan and sketch first, then build. Mentors are in the room.</li>
        <li><strong>12:30 PM, Lunch:</strong> Food is provided. Keep building if you like.</li>
        <li><strong>1:45 to 2:00 PM, Final submissions:</strong> Hand in your team summary and set up your demo.</li>
        <li><strong>2:00 to 3:15 PM, Team demos:</strong> Show what you built and answer questions.</li>
        <li><strong>3:15 to 3:40 PM, Judging and networking:</strong> Judges score while everyone mingles.</li>
        <li><strong>3:40 to 4:00 PM, Awards and closing:</strong> Winners, photos, and thanks.</li>
    </ul>
    <p>Want the full rules and the scoring rubric? <a href="{{ site.pack_pdf | relative_url }}">Download the Participant Pack (PDF)</a>.</p>
</section>

<section id="know-before-you-go" class="site-section" data-aos="fade-up">
    <h2>Know Before You Go</h2>
    <ul>
        <li><strong>Where:</strong> Microsoft Calgary Office, 110 9 Ave SW, in the Le Germain office tower across 9 Avenue from the Calgary Tower.</li>
        <li><strong>Getting in:</strong> The building is locked on Saturday. Wait in the main lobby from 9:00 AM and a volunteer brings you up. Running late? Message David in the Meetup event chat.</li>
        <li><strong>Washrooms:</strong> They are in the hallway outside the office, and the office door locks behind you. Tell a volunteer before you step out.</li>
        <li><strong>Parking:</strong> Brookfield Place underground (Lot #35, 225 6 Ave SW, about 3 blocks north) is about $3.15 for 24 hours on the weekend. The surface lot at 208 9 Ave SW is about $5 to $15 for the day. Check the posted rates.</li>
        <li><strong>Transit:</strong> The 7 Avenue CTrain stations at Centre Street and 1 Street SW are about a 5 minute walk.</li>
        <li><strong>Bring:</strong> A laptop and charger. Use your work or school environment only if your organization allows it. No environment? Sign up for the free <a href="https://aka.ms/PowerAppsDevPlan" target="_blank" rel="noopener">Power Apps Developer Plan</a> before you arrive.</li>
        <li><strong>Check in:</strong> Fill in the <a href="https://forms.cloud.microsoft/r/B4kKv3YLdp" target="_blank" rel="noopener">registration form</a> tonight, or scan the QR code at the door.</li>
    </ul>
    <p>All of this is on page 1 of the <a href="{{ site.pack_pdf | relative_url }}">Participant Pack (PDF)</a>.</p>
</section>

<section id="prizes" class="site-section" data-aos="fade-up">
    <h2>Amazing Prizes Await!</h2>
    <ul>
        <li><strong>🏆 Two individual passes:</strong> Power Platform Community Conference 2026 (PPCC26) conference passes, provided by Microsoft. Travel and accommodation are not included.</li>
        <li><strong>🥈 Runners-up:</strong> Lego Clippy mascots for that perfect desk companion.</li>
    </ul>
<p style="font-style: italic; color: var(--primary-color); margin-top: 1rem; padding: 1rem; background: var(--background-light); border-radius: var(--border-radius); border-left: 4px solid var(--primary-color);">Every participant walks away with new skills, connections, and the satisfaction of building something incredible!</p>
</section>

<section id="sponsors" class="site-section" data-aos="fade-up">
    <h2>Thank You to Our Sponsors</h2>
    <p>Microsoft Calgary hosts the hackathon and provides the PPCC26 passes. Thank you to our sponsors, Bauer Automate and Gravity Union, and to Egg Club (downtown location) for the lunch sandwiches.</p>
    <div class="sponsor-logos" style="display: flex; gap: 2rem; margin-bottom: 1.5rem; align-items: center; flex-wrap: wrap; justify-content: center;">
        <a href="https://www.microsoft.com/" target="_blank" rel="noopener" title="Microsoft: venue host and PPCC26 passes">
            <img src="{{ '/assets/images/sponsors/microsoft.svg' | relative_url }}" alt="Microsoft Logo" style="height: 40px;" loading="lazy">
        </a>
        <img src="{{ '/assets/images/sponsors/egg-club.png' | relative_url }}" alt="Egg Club Logo" title="Egg Club: lunch sandwiches" style="height: 70px;" loading="lazy">
        <a href="https://www.bauerautomate.com/" target="_blank" rel="noopener">
            <img src="{{ '/assets/images/sponsors/bauer-automate.png' | relative_url }}" alt="Bauer Automate Logo" style="height: 60px;" loading="lazy">
        </a>
        <a href="https://gravityunion.com/" target="_blank" rel="noopener">
            <img src="{{ '/assets/images/sponsors/gravity-union.webp' | relative_url }}" alt="Gravity Union Logo" style="height: 60px;" loading="lazy">
        </a>
    </div>
</section>


<section id="community" class="site-section" data-aos="fade-up">
    <h2>Community</h2>
    
    <div style="text-align: center; margin-bottom: 3rem; background: var(--background-light); padding: 2rem; border-radius: var(--border-radius);" data-aos="fade-right" data-aos-delay="200">
        <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 1.5rem; flex-wrap: wrap;">
            <img src="{{ '/assets/images/logos/calgary-power-platform-logo.webp' | relative_url }}" alt="Calgary Power Platform User Group Logo" style="height: 60px;" loading="lazy">
            <div>
                <h3 style="margin: 0; font-size: 1.5rem;">Calgary Power Platform User Group</h3>
                <p style="margin: 0.5rem 0; color: var(--text-light);">Calgary, AB, Canada</p>
            </div>
        </div>
        
        <div style="display: flex; justify-content: center; gap: 3rem; margin: 2rem 0; flex-wrap: wrap;">
            <div style="text-align: center;">
                <div style="font-size: 2rem; color: var(--accent-color); margin-bottom: 0.5rem;">⭐ 4.7</div>
                <p style="margin: 0; font-weight: 600;">Rating</p>
                <p style="margin: 0; color: var(--text-light); font-size: 0.9rem;">(24 reviews)</p>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 2rem; color: var(--primary-color); margin-bottom: 0.5rem;">👥 255</div>
                <p style="margin: 0; font-weight: 600;">Members</p>
                <p style="margin: 0; color: var(--text-light); font-size: 0.9rem;">and growing!</p>
            </div>
        </div>
        
        <div class="cta">
            <a href="https://www.meetup.com/calgary-power-platform-user-group/?msockid=2ef044982fbe645016e852862e0a6585" target="_blank" class="cta-button">
                <i class="fab fa-meetup"></i> Join Our Meetup Group
            </a>
        </div>
    </div>

    <div style="margin: 3rem 0;">
        <h3 style="color: var(--primary-color); text-align: center; margin-bottom: 1.5rem;">📸 Community Event Highlights</h3>
        <p style="text-align: center; margin-bottom: 2rem;">Take a look at some memorable moments from our past Power Platform events and community gatherings!</p>
        
        <div class="event-gallery" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 2rem 0;">
            <div class="gallery-item">
                <a href="{{ '/assets/images/events/event_523846657.webp' | relative_url }}" target="_blank">
                    <img src="{{ '/assets/images/events/event_523846657.webp' | relative_url }}" alt="CPPUG Community Event" loading="lazy" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.1); transition: transform 0.3s ease; cursor: pointer;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                </a>
            </div>
            <div class="gallery-item">
                <a href="{{ '/assets/images/events/event_526942368.webp' | relative_url }}" target="_blank">
                    <img src="{{ '/assets/images/events/event_526942368.webp' | relative_url }}" alt="Power Platform Workshop" loading="lazy" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.1); transition: transform 0.3s ease; cursor: pointer;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                </a>
            </div>
            <div class="gallery-item">
                <a href="{{ '/assets/images/events/event_528364604.webp' | relative_url }}" target="_blank">
                    <img src="{{ '/assets/images/events/event_528364604.webp' | relative_url }}" alt="Community Networking Event" loading="lazy" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.1); transition: transform 0.3s ease; cursor: pointer;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                </a>
            </div>
            <div class="gallery-item">
                <a href="{{ '/assets/images/events/event_528364609.webp' | relative_url }}" target="_blank">
                    <img src="{{ '/assets/images/events/event_528364609.webp' | relative_url }}" alt="Learning Session" loading="lazy" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.1); transition: transform 0.3s ease; cursor: pointer;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                </a>
            </div>
            <div class="gallery-item">
                <a href="{{ '/assets/images/events/event_529417355.webp' | relative_url }}" target="_blank">
                    <img src="{{ '/assets/images/events/event_529417355.webp' | relative_url }}" alt="Team Collaboration" loading="lazy" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.1); transition: transform 0.3s ease; cursor: pointer;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                </a>
            </div>
            <div class="gallery-item">
                <a href="{{ '/assets/images/events/event_529417356.webp' | relative_url }}" target="_blank">
                    <img src="{{ '/assets/images/events/event_529417356.webp' | relative_url }}" alt="Knowledge Sharing" loading="lazy" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.1); transition: transform 0.3s ease; cursor: pointer;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                </a>
            </div>
            <div class="gallery-item">
                <a href="{{ '/assets/images/events/event_529417357.webp' | relative_url }}" target="_blank">
                    <img src="{{ '/assets/images/events/event_529417357.webp' | relative_url }}" alt="Knowledge Sharing" loading="lazy" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.1); transition: transform 0.3s ease; cursor: pointer;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                </a>
            </div>
            <div class="gallery-item">
                <a href="{{ '/assets/images/events/event_529417358.webp' | relative_url }}" target="_blank">
                    <img src="{{ '/assets/images/events/event_529417358.webp' | relative_url }}" alt="Knowledge Sharing" loading="lazy" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.1); transition: transform 0.3s ease; cursor: pointer;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                </a>
            </div>
            <div class="gallery-item">
                <a href="{{ '/assets/images/events/event_529417359.webp' | relative_url }}" target="_blank">
                    <img src="{{ '/assets/images/events/event_529417359.webp' | relative_url }}" alt="Knowledge Sharing" loading="lazy" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.1); transition: transform 0.3s ease; cursor: pointer;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                </a>
            </div>
        </div>
        
        <p style="text-align: center; font-style: italic; color: var(--text-light); margin-top: 2rem;">
            Join our vibrant community and be part of Calgary's growing Power Platform ecosystem!
        </p>
    </div>
</section>

<section id="volunteer" class="site-section" data-aos="fade-up">
    <h2>🤝 Volunteer with Us</h2>
    <p>Help make the CPPUG Hackathon Challenge an amazing experience for everyone! We're looking for passionate community members to join our volunteer team.</p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 3rem 0;">
        <div data-aos="fade-right" data-aos-delay="200">
            <h3 style="color: var(--primary-color); margin-bottom: 1.5rem;">🌟 Why Volunteer?</h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 1rem; padding-left: 0;">🎯 <strong>Make an Impact:</strong> Help create an incredible experience for participants</li>
                <li style="margin-bottom: 1rem; padding-left: 0;">🤝 <strong>Network:</strong> Connect with community leaders and fellow enthusiasts</li>
                <li style="margin-bottom: 1rem; padding-left: 0;">📚 <strong>Learn:</strong> Gain behind-the-scenes event management experience</li>
                <li style="margin-bottom: 1rem; padding-left: 0;">🏆 <strong>Recognition:</strong> Be acknowledged as a key community contributor</li>
                <li style="margin: 0; padding-left: 0;">💼 <strong>Give Back:</strong> Support Calgary's growing tech community</li>
            </ul>
        </div>

        <div data-aos="fade-left" data-aos-delay="400">
            <h3 style="color: var(--primary-color); margin-bottom: 1.5rem;">📋 Volunteer Opportunities</h3>
            <div style="background: var(--background-light); padding: 1.5rem; border-radius: var(--border-radius); border-left: 4px solid var(--accent-color);">
                <p style="margin-bottom: 0.75rem;"><strong>🎪 Event Setup:</strong> Help prepare the venue and materials</p>
                <p style="margin-bottom: 0.75rem;"><strong>👋 Registration & Welcome:</strong> Greet participants and handle check-in</p>
                <p style="margin-bottom: 0.75rem;"><strong>🍕 Food & Logistics:</strong> Coordinate meals and refreshments</p>
                <p style="margin-bottom: 0.75rem;"><strong>💡 Technical Support:</strong> Assist teams with platform questions</p>
                <p style="margin-bottom: 0.75rem;"><strong>📸 Documentation:</strong> Capture event highlights for our community</p>
                <p style="margin: 0;"><strong>🏆 Awards & Closing:</strong> Help with judging logistics and ceremony</p>
            </div>
        </div>
    </div>

    <div class="cta" style="text-align: center; margin-top: 3rem;">
        <a href="https://forms.office.com/r/CSB1VHXqjx" target="_blank" class="cta-button">
            <i class="fas fa-hand-heart"></i> Sign Up to Volunteer
        </a>
        <a href="{{ site.team_pdf | relative_url }}" class="cta-button">
            <i class="fas fa-file-pdf"></i> Volunteer and Judge Pack
        </a>
    </div>
</section>

<section id="contact" class="site-section" data-aos="fade-up">
    <h2>📞 Questions & Support</h2>
    <p>Still have questions? We're here to help!</p>
    
    <div style="background: var(--background-light); padding: 2rem; border-radius: var(--border-radius); margin: 2rem 0;">
        <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
            <li style="display: flex; align-items: center; gap: 0.75rem;">
                <i class="fas fa-envelope" style="color: var(--accent-color); width: 20px; font-size: 1.2rem;"></i>
                <div>
                    <strong>Email:</strong><br>
                    <a href="mailto:communityleader@cppug.onmicrosoft.com" style="color: var(--primary-color);">communityleader@cppug.onmicrosoft.com</a>
                </div>
            </li>
            <li style="display: flex; align-items: center; gap: 0.75rem;">
                <i class="fab fa-meetup" style="color: var(--accent-color); width: 20px; font-size: 1.2rem;"></i>
                <div>
                    <strong>Meetup:</strong><br>
                    <a href="https://www.meetup.com/calgary-power-platform-user-group/" target="_blank" style="color: var(--primary-color);">Calgary Power Platform User Group</a>
                </div>
            </li>
            <li style="display: flex; align-items: center; gap: 0.75rem;">
                <i class="fas fa-users" style="color: var(--accent-color); width: 20px; font-size: 1.2rem;"></i>
                <div>
                    <strong>During Event:</strong><br>
                    <span style="color: var(--text-light);">Organizers and mentors available throughout the day</span>
                </div>
            </li>
        </ul>
    </div>
</section>
