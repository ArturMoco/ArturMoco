import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='markdown-readme-mrgenerator',
    keywords='markdown readme mrgenerator generator',
    version='0.1.4',
    # 1.2.0.dev1  # Development release
    # 1.2.0a1     # Alpha Release
    # 1.2.0b1     # Beta Release
    # 1.2.0rc1    # Release Candidate
    # 1.2.0       # Final Release
    packages=setuptools.find_packages(),
    package_data={
        "": ["*.pmd"],
    },
    url='https://github.com/ArturMoco',
    license='EBAC - Escola Britânica de Artes Criativas e Técnologias',
    author='Artur Felipe Albuquerque Portela',
    author_email='arturengqa@gmail.com',
    description='QA Tester',
    long_description="I am a Software Test Analyst recently graduated from the British School of Creative Arts and Technology, an event producer affiliated to the Brazilian Association of Event Producers, and graduating in Agronomy from the Federal University of Ceará. I am always attentive to new technologies and market demands. I live in continuous updates on all areas of my interest. I constantly seek to insert cultural and social aspects into the new available technologies, building a work environment inserted in the most current and modern.  I am observant, proactive, resilient and adapt quickly to changes. I easily find practical, effective and innovative solutions in the most diverse environments. I'm a good communicator with zero inhibitions in front of microphones. I am in continuous learning and development of my activities as QA. In addition to the professional course, I sought to improve myself in programming and software development techniques, exploring the most used languages ​​in the market. In addition, I have 10 years of experience as an entrepreneur, working as a producer of cultural and entertainment events. I directly contributed to expand the music festival scene in the interior of the state of Ceará. I encouraged and introduced the use of accessible technologies for management and control in event management at all stages, being a pioneer in my region. Much of what I learned in that time as a producer and entrepreneur was by observing and getting to know the work of other producers throughout Brazil. I also develop voluntary work in my municipality as a mobilizer of NUCA (Núcleo da Criança e do Adolescente), a UNICEF program, to help build a healthy childhood and a citizen adolescence. I am also a paraglider pilot, I was once a professional and today I practice the sport only as a hobby, I participated in several competitions between 2016 and 2018, Free flight taught me to focus, discipline and adapt to completely adverse situations.",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: JavaScript :: Node.Js :: JSON :: Cucumber :: Gherkin :: HTML5 :: CSS3",
        "License :: EBAC - Escola Britanica de Artes Criativas e Técnologias :: Universidade Federal do Ceará - Agronomia",
        "Operating System :: Windows, Android, Linux, IOS",
    ],
    project_urls={
        'E2E Testes': 'https://github.com/ArturMoco/testes-e2e-ebac-shop',
        'UI Testes': 'https://github.com/ArturMoco/teste-ebac-ui',
    },
    python_requires='~=3.6',
    install_requires=requirements,
    entry_points={'console_scripts': ['mrgenerator-cli = mrgenerator.run:cli']}
)
