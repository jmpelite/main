# Create remaining React components

# Credentials component
credentials_js = """import React from 'react';

const Credentials = () => {
  const credentialsList = [
    { title: 'Level 3 Personal Trainer', icon: '🏋️‍♂️' },
    { title: 'Level 3 Nutrition Specialist', icon: '🥗' },
    { title: 'Level 2 Fitness Instructor', icon: '💪' },
    { title: 'Level 2 Mental Health Awareness', icon: '🧠' },
    { title: 'Harm-Reduction and Wellbeing Advocate', icon: '❤️' },
  ];

  return (
    <section id="credentials" className="max-w-5xl mx-auto px-4 py-16">
      <div className="bg-gray-800 rounded-2xl shadow-2xl p-8 md:p-12 card-hover">
        <h2 className="text-3xl md:text-4xl font-bold text-blue-400 mb-8 text-center">Qualifications</h2>
        <div className="grid gap-4 md:gap-6">
          {credentialsList.map((cred, index) => (
            <div key={index} className="flex items-center p-4 bg-gray-700 rounded-lg hover:bg-gray-600 transition-colors duration-200">
              <span className="text-2xl mr-4">{cred.icon}</span>
              <span className="text-gray-200 font-medium text-lg">{cred.title}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Credentials;"""

# Tips component
tips_js = """import React from 'react';

const Tips = () => {
  const tipsList = [
    {
      title: 'Post-Night Recovery',
      content: 'Hydrate, eat, nap & don\\'t stress. It\\'s about progress, not perfection.',
      icon: '🌅'
    },
    {
      title: 'Lifting with a Hangover?',
      content: 'Go lighter, shorter session, finish with fresh air. Show up, but listen to your body.',
      icon: '🏃‍♂️'
    },
    {
      title: 'No Guilt, Only Balance',
      content: 'Enjoy your weekend. Get back on track—not beat yourself up.',
      icon: '⚖️'
    },
    {
      title: 'Mental Health = Physical Health',
      content: 'Movement helps mood. No pressure to always be "on it."',
      icon: '🧘‍♂️'
    },
    {
      title: 'Mythbusting',
      content: '"Carbs aren\\'t evil." "One night out won\\'t ruin progress."',
      icon: '🔬'
    },
    {
      title: 'Sleep & Recovery',
      content: 'Quality sleep beats perfect nutrition. Prioritize rest for real gains.',
      icon: '😴'
    }
  ];

  return (
    <section id="tips" className="max-w-7xl mx-auto px-4 py-16">
      <div className="bg-gray-800 rounded-2xl shadow-2xl p-8 md:p-12">
        <h2 className="text-3xl md:text-4xl font-bold text-blue-400 mb-8 text-center">Party Life & Gym Gains Hacks</h2>
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {tipsList.map((tip, index) => (
            <div key={index} className="bg-gray-700 rounded-xl p-6 card-hover hover:bg-gray-600 transition-all duration-300">
              <div className="text-3xl mb-4 text-center">{tip.icon}</div>
              <h3 className="text-xl font-bold text-blue-300 mb-3 text-center">{tip.title}</h3>
              <p className="text-gray-300 leading-relaxed text-center">{tip.content}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Tips;"""

# Testimonials component
testimonials_js = """import React from 'react';

const Testimonials = () => {
  const testimonials = [
    {
      text: "I finally started feeling confident—without changing my social life. JMP gets it, no lectures.",
      name: "Steph",
      age: "25",
      location: "Glasgow"
    },
    {
      text: "Always honest, never judgy. Best advice for balancing parties and progress.",
      name: "Calum",
      age: "22",
      location: "Dundee"
    },
    {
      text: "After working with JMP, my sleep and mood are up, and I don't feel guilty about nights out.",
      name: "Megan",
      age: "19",
      location: "Edinburgh"
    },
    {
      text: "Finally found someone who understands student life. Real advice that actually works.",
      name: "Jamie",
      age: "21",
      location: "Stirling"
    }
  ];

  return (
    <section id="testimonials" className="max-w-7xl mx-auto px-4 py-16">
      <div className="bg-gray-800 rounded-2xl shadow-2xl p-8 md:p-12">
        <h2 className="text-3xl md:text-4xl font-bold text-blue-400 mb-8 text-center">Real Results, Real People</h2>
        <div className="grid gap-6 md:grid-cols-2">
          {testimonials.map((testimonial, index) => (
            <div key={index} className="bg-gray-700 rounded-xl p-6 card-hover border-l-4 border-blue-400">
              <p className="text-gray-300 leading-relaxed mb-4 italic text-lg">
                "{testimonial.text}"
              </p>
              <div className="text-blue-300 font-semibold">
                – {testimonial.name}, {testimonial.age}, {testimonial.location}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Testimonials;"""

# Save these components
with open('Credentials.js', 'w') as f:
    f.write(credentials_js)

with open('Tips.js', 'w') as f:
    f.write(tips_js)

with open('Testimonials.js', 'w') as f:
    f.write(testimonials_js)

print("Credentials, Tips, and Testimonials components created!")