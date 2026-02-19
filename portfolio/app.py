from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "any-random-string"

def get_lang():
    return session.get("lang", "en")
translations = {
    "en": {
        "site_title": "Portfolio",
        "menu_home": "Home",

        "menu_projects": "My projects",
        "menu_cv": "CV",
        "menu_contact": "Contact me",

        "home_title": "Architecture",
        "home_name": "Andrey Ponomarenko",

        "contact_title": "Contact me",
        "contact_email": "Email",
        "contact_whatsapp": "WhatsApp",
        "home_page_title": "Home",
        "home_subtitle": "Senior Technical Architect / Architect / Architectural Technician",

        "projects_page_title": "Projects",
        "projects_title": "My projects",
        "projects_intro": "This section will display projects from 2003 to 2026, including already constructed buildings, visualizations and drawings.",
        "projects_item_1": "Residential design projects",
        "projects_item_2": "Working drawings and documentation",
        "projects_item_3": "Site plans and surveys",

        "resume_page_title": "CV",
        "resume_title": "CV",
        "resume_summary_title": "Summary",
        "resume_summary_p1": "Experienced architect with 22+ years of practice.",
        "resume_summary_p2": "UK / EU / Ukraine experience. Open to relocation.",
        "resume_skills_title": "Skills",
        "resume_skill_1": "Working documentation (specialization)",
        "resume_skill_2": "AutoCAD, ArchiCAD, Photoshop, Lumion",
        "resume_skill_3": "English B2, Full UK driving licence (B)",
        "resume_experience_title": "Work History",
        "resume_experience_note": "Full work history is available in the detailed version of the CV.",
        "resume_page_title": "CV",
"resume_title": "CV",
"resume_name": "Andrey Ponomarenko",
"resume_role": "Senior Technical Architect / Architect / Architectural Technician",
"resume_p1": "Hello, my name is Andrey. I am a 44-year-old architect, born in Kyiv (USSR, later Ukraine). I am an experienced architect with over 22 years of professional practice.",
"resume_p2": "My career started in 2003, and since then I have worked on a wide range of projects, both independently and as a manager of design companies and departments. I have experience working in the UK, EU, and Ukraine.",
"resume_p3": "I design residential, public, and industrial buildings of varying complexity. I am currently living in the UK and am open to relocation. I am seeking an opportunity in architecture or construction where I can fully utilize my skills and experience and contribute long-term to a company.",

"resume_skills_title": "Skills",
"resume_skill_1": "Working documentation (specialization)",
"resume_skill_2": "AutoCAD",
"resume_skill_3": "ArchiCAD",
"resume_skill_4": "Adobe Photoshop",
"resume_skill_5": "Lumion",
"resume_skill_6": "ArtLantis",
"resume_skill_7": "Microsoft Office",
"resume_skill_8": "Cambridge English Certificate B2",
"resume_skill_9": "Full UK driving licence (Category B), own car",
"resume_skill_10": "Languages: English (B2), Russian (native), Ukrainian (native), Spanish (beginner), Arabic (beginner)",

"resume_work_title": "Work History",

"job1_title": "Architect / Architectural Technician",
"job1_company": "Wellwood Leslie Architects, Scotland (Aberdeen / Dundee / Glasgow)",
"job1_dates": "September 2023 – Present",
"job1_b1": "Designing residential and civil buildings",
"job1_b2": "Site development plans",
"job1_b3": "Building surveys and drawings",
"job1_b4": "Fire remedial works",

"job2_title": "Architect Assistant",
"job2_company": "GWS Architects, Aberdeen, Scotland",
"job2_dates": "March 2023 – July 2023",
"job2_b1": "Low-rise residential projects (Aberdeenshire)",
"job2_b2": "Elevations for Bristow helicopter airport (Dyce)",
"job2_b3": "Architectural sections",

"job3_title": "Architect",
"job3_company": "Nouveauarch, Oradea, Romania",
"job3_dates": "March 2022 – July 2022",
"job3_b1": "Low-rise residential buildings",
"job3_b2": "Plantations and farms",
"job3_b3": "Architectural sections",

"job4_title": "Architect / Chief Architect / Expert",
"job4_company": "MPI, D-I-M, Dan Project, Ukrbudconsult Inspection",
"job4_dates": "November 2020 – February 2022",
"job4_b1": "Residential and civil buildings design",
"job4_b2": "Leading multiple design teams",
"job4_b3": "Construction management",
"job4_b4": "Inspection and assessor services",

"job5_title": "Chief Architect",
"job5_company": "Viharev Restoration",
"job5_dates": "March 2020 – November 2020",
"job5_b1": "Design department coordination",
"job5_b2": "Office buildings in Kyiv",
"job5_b3": "Reconstruction and restoration of historical buildings",
"job5_b4": "Remote team leadership during Covid-19",

"job6_title": "Advisor to the Head of the State Architectural and Construction Inspectorate",
"job6_company": "DABI Ukraine",
"job6_dates": "December 2019 – March 2020",
"job6_b1": "Verification of project documentation",
"job6_b2": "Issuing building permits",
"job6_b3": "Government agency experience",

"job7_title": "Architect / Chief Architect / Director",
"job7_company": "IISRR",
"job7_dates": "May 2016 – December 2019",
"job7_b1": "Design and management of residential and civil projects",
"job7_b2": "Leading design teams",
"job7_b3": "Company administration",

"job8_title": "Chief Architect",
"job8_company": "Prometei – Siaivo, Kyiv",
"job8_dates": "September 2013 – April 2016",
"job8_b1": "Historical buildings in central Kyiv",
"job8_b2": "Project and working documentation",
"job8_b3": "State examination approval",

"job9_title": "Chief Architect",
"job9_company": "Oksi-K",
"job9_dates": "June 2011 – March 2013",
"job9_b1": "Office centres, warehouses, car dealerships, residential buildings",
"job9_b2": "Author’s supervision",
"job9_b3": "Construction management",

"resume_edu_title": "Education & Training",
"edu1": "2022–2023 — North East College of Scotland, ESOL B2",
"edu2": "2014 — Architect’s Licence (Ukraine)",
"edu3": "1998–2003 — Kyiv National University of Construction and Architecture",

"resume_refs_title": "References:",
"resume_refs_text": "Available upon request",

"projects_built_title": "Already built buildings",
"project1_title": "Residential Building in Kiev, Ukraine",
"project2_title": "Residential Complex  in Kiev, Ukraine (before)",
"project3_title": "Residential Complex  in Kiev, Ukraine (after)",
"project4_title": "Residential Building in Kiev City Centre, Ukraine",
"project7_title": "Residential Complex in Kiev, Ukraine",
"project10_title": "Residential Complex 'Silver Breeze', Kiev, Ukraine",
"project13_title": "Renault Centre, Belaya Tserkov, Ukraine",
"projects_visualizations_title": "Visualizations",
"projects_drawings_title": "Drawings",




"project22_title": "Cottage in Kiev Region, Ukraine",
"project23_title": "Residential Complex in Kiev, Ukraine",
"project24_title": "Residential Complex in Kiev, Ukraine",
"project25_title": "Cottage Complex in Kiev Region, Ukraine",
"project26_title": "Residential Complex in Kiev, Ukraine",
"project27_title": "Residential Complex in Kiev, Ukraine",
"project28_title": "Residential Complex in Kiev, Ukraine",
"project29_title": "Renault Dealer's Centre, Belaya Tserkov, Ukraine",
"project30_title": "Residential Complex in Kozin, Ukraine",
"project31_title": "Residential Complex in Kozin, Ukraine",
"project32_title": "Business Centre in Kiev, Ukraine",
"project33_title": "Business Centre in Kiev, Ukraine",
"project34_title": "Business Centre in Kiev, Ukraine",
"project35_title": "Business Centre in Kiev, Ukraine",
"project36_title": "Health Centre in Kiev, Ukraine",
"project37_title": "Health Centre in Kiev, Ukraine",
"project38_title": "Health Centre in Kiev, Ukraine",
"project39_title": "Health Centre in Kiev, Ukraine",



    },
    "es": {
        "site_title": "Portafolio",
        "menu_home": "Inicio",

        "menu_projects": "Proyectos",
        "menu_cv": "CV",
        "menu_contact": "Contacto",

        "home_title": "Arquitectura",
        "home_name": "Andrey Ponomarenko",

        "contact_title": "Contáctame",

        "contact_email": "Correo",
        "contact_whatsapp": "WhatsApp",
        "home_page_title": "Inicio",
        "home_subtitle": "Arquitecto técnico senior / Arquitecto / Técnico de arquitectura",

        "projects_page_title": "Proyectos",
        "projects_title": "Mis proyectos",
        "projects_intro": "En esta sección se mostrarán proyectos desde 2003 hasta 2026, incluyendo edificios ya construidos, representaciones y dibujos.",
        "projects_item_1": "Proyectos de diseño residencial",
        "projects_item_2": "Planos y documentación técnica",
        "projects_item_3": "Planos de emplazamiento y levantamientos",

        "resume_page_title": "CV",
        "resume_title": "CV",
        "resume_summary_title": "Resumen",
        "resume_summary_p1": "Arquitecto con más de 22 años de experiencia.",
        "resume_summary_p2": "Experiencia en Reino Unido / UE / Ucrania. Disponible para reubicación.",
        "resume_skills_title": "Habilidades",
        "resume_skill_1": "Documentación técnica (especialización)",
        "resume_skill_2": "AutoCAD, ArchiCAD, Photoshop, Lumion",
        "resume_skill_3": "Inglés B2, permiso de conducir del Reino Unido (B)",
        "resume_experience_title": "Experiencia laboral",
        "resume_experience_note": "El historial completo está disponible en la versión detallada del CV.",
        "resume_page_title": "CV",
"resume_title": "CV",
"resume_name": "Andrey Ponomarenko",
"resume_role": "Arquitecto Técnico Senior / Arquitecto / Técnico en Arquitectura",
"resume_p1": "Hola, mi nombre es Andrey. Soy un arquitecto de 44 años, nacido en Kyiv (URSS, posteriormente Ucrania). Soy un arquitecto con más de 22 años de experiencia profesional.",
"resume_p2": "Mi carrera comenzó en 2003 y, desde entonces, he trabajado en una amplia variedad de proyectos, tanto de forma independiente como gestionando empresas y departamentos de diseño. Tengo experiencia profesional en el Reino Unido, la Unión Europea y Ucrania.",
"resume_p3": "Diseño edificios residenciales, públicos e industriales de diferentes niveles de complejidad. Actualmente resido en el Reino Unido y estoy disponible para reubicación. Busco una oportunidad en el ámbito de la arquitectura o la construcción donde pueda utilizar plenamente mis conocimientos y experiencia y contribuir a largo plazo al desarrollo de la empresa.",

"resume_skills_title": "Habilidades",
"resume_skill_1": "Documentación técnica (especialización)",
"resume_skill_2": "AutoCAD",
"resume_skill_3": "ArchiCAD",
"resume_skill_4": "Adobe Photoshop",
"resume_skill_5": "Lumion",
"resume_skill_6": "ArtLantis",
"resume_skill_7": "Microsoft Office",
"resume_skill_8": "Certificado de Inglés de Cambridge B2",
"resume_skill_9": "Permiso de conducir del Reino Unido (categoría B), vehículo propio",
"resume_skill_10": "Idiomas: Inglés (B2), Ruso (nativo), Ucraniano (nativo), Español (básico), Árabe (básico)",

"resume_work_title": "Experiencia profesional",

"job1_title": "Arquitecto / Técnico en Arquitectura",
"job1_company": "Wellwood Leslie Architects, Escocia (Aberdeen / Dundee / Glasgow)",
"job1_dates": "Septiembre 2023 – Actualidad",
"job1_b1": "Diseño de edificios residenciales y civiles",
"job1_b2": "Planes de desarrollo del emplazamiento",
"job1_b3": "Levantamientos y documentación gráfica",
"job1_b4": "Trabajos de remediación contra incendios",

"job2_title": "Asistente de Arquitecto",
"job2_company": "GWS Architects, Aberdeen, Escocia",
"job2_dates": "Marzo 2023 – Julio 2023",
"job2_b1": "Proyectos residenciales de baja altura (Aberdeenshire)",
"job2_b2": "Diseño de alzados para el aeropuerto de helicópteros Bristow (Dyce)",
"job2_b3": "Desarrollo de secciones arquitectónicas",

"job3_title": "Arquitecto",
"job3_company": "Nouveauarch, Oradea, Rumanía",
"job3_dates": "Marzo 2022 – Julio 2022",
"job3_b1": "Diseño de edificios residenciales de baja altura",
"job3_b2": "Diseño de plantaciones y explotaciones agrícolas",
"job3_b3": "Desarrollo de secciones arquitectónicas",

"job4_title": "Arquitecto / Arquitecto Jefe / Experto",
"job4_company": "MPI, D-I-M, Dan Project, Ukrbudconsult Inspection",
"job4_dates": "Noviembre 2020 – Febrero 2022",
"job4_b1": "Diseño de edificios residenciales y civiles",
"job4_b2": "Dirección de varios equipos de diseño",
"job4_b3": "Gestión de obra",
"job4_b4": "Servicios de inspección y evaluación",

"job5_title": "Arquitecto Jefe",
"job5_company": "Viharev Restoration",
"job5_dates": "Marzo 2020 – Noviembre 2020",
"job5_b1": "Coordinación del departamento de diseño",
"job5_b2": "Diseño de edificios de oficinas en Kyiv",
"job5_b3": "Reconstrucción y restauración de edificios históricos",
"job5_b4": "Gestión remota de equipos durante la pandemia de Covid-19",

"job6_title": "Asesor del Director de la Inspección Estatal de Arquitectura y Construcción",
"job6_company": "DABI Ucrania",
"job6_dates": "Diciembre 2019 – Marzo 2020",
"job6_b1": "Verificación de documentación de proyectos",
"job6_b2": "Emisión de permisos de construcción",
"job6_b3": "Experiencia en organismos gubernamentales",

"job7_title": "Arquitecto / Arquitecto Jefe / Director",
"job7_company": "IISRR",
"job7_dates": "Mayo 2016 – Diciembre 2019",
"job7_b1": "Diseño y gestión de proyectos residenciales y civiles",
"job7_b2": "Dirección de equipos de diseño",
"job7_b3": "Administración de la empresa",

"job8_title": "Arquitecto Jefe",
"job8_company": "Prometei – Siaivo, Kyiv",
"job8_dates": "Septiembre 2013 – Abril 2016",
"job8_b1": "Edificios históricos en el centro de Kyiv",
"job8_b2": "Documentación de proyecto y ejecución",
"job8_b3": "Aprobación de exámenes estatales",

"job9_title": "Arquitecto Jefe",
"job9_company": "Oksi-K",
"job9_dates": "Junio 2011 – Marzo 2013",
"job9_b1": "Centros de oficinas, almacenes, concesionarios de automóviles y edificios residenciales",
"job9_b2": "Supervisión de autor",
"job9_b3": "Gestión de obra",

"resume_edu_title": "Educación y formación",
"edu1": "2022–2023 — North East College of Scotland, ESOL B2",
"edu2": "2014 — Licencia de Arquitecto (Ucrania)",
"edu3": "1998–2003 — Universidad Nacional de Construcción y Arquitectura de Kyiv",

"resume_refs_title": "Referencias:",
"resume_refs_text": "Disponibles a solicitud",

"projects_built_title": "Edificios ya construidos",
"project1_title": "Edificio residencial en Kiev, Ucrania",
"project2_title": "Complejo residencial en Kiev, Ucrania (antes)",
"project3_title": "Complejo residencial en Kiev, Ucrania (después)",
"project4_title": "Edificio residencial en el centro de Kiev, Ucrania",
"project7_title": "Complejo residencial en Kiev, Ucrania",
"project10_title": "Complejo residencial 'Silver Breeze', Kiev, Ucrania",
"project13_title": "Centro Renault, Belaya Tserkov, Ucrania",
"projects_visualizations_title": "Visualizaciones",
"projects_drawings_title": "Planos",

"project22_title": "Casa rural en la región de Kiev, Ucrania",
"project23_title": "Complejo residencial en Kiev, Ucrania",
"project24_title": "Complejo residencial en Kiev, Ucrania",
"project25_title": "Complejo rural en la región de Kiev, Ucrania",
"project26_title": "Complejo residencial en Kiev, Ucrania",
"project27_title": "Complejo residencial en Kiev, Ucrania",
"project28_title": "Complejo residencial en Kiev, Ucrania",
"project29_title": "Concesionario Renault, Belaya Tserkov, Ucrania",
"project30_title": "Complejo residencial en Kozin, Ucrania",
"project31_title": "Complejo residencial en Kozin, Ucrania",
"project32_title": "Centro de negocios en Kiev, Ucrania",
"project33_title": "Centro de negocios en Kiev, Ucrania",
"project34_title": "Centro de negocios en Kiev, Ucrania",
"project35_title": "Centro de negocios en Kiev, Ucrania",
"project36_title": "Centro de salud en Kiev, Ucrania",
"project37_title": "Centro de salud en Kiev, Ucrania",
"project38_title": "Centro de salud en Kiev, Ucrania",
"project39_title": "Centro de salud en Kiev, Ucrania",






    }
}

   

def t(key):
    lang = get_lang()
    return translations.get(lang, translations["en"]).get(key, key)

@app.route("/set-lang/<lang>")
def set_lang(lang):
    if lang not in ("en", "es"):
        lang = "en"
    session["lang"] = lang
    return redirect(request.referrer or url_for("home"))

@app.route("/")
def home():
    return render_template("index.html", lang=get_lang(), t=t)

@app.route("/projects")
def projects():
    return render_template("projects.html", lang=get_lang(), t=t)

@app.route("/contact")
def contact():
    return render_template("contact.html", lang=get_lang(), t=t)

@app.route("/resume")
def resume():
    return render_template("resume.html", lang=get_lang(), t=t)

if __name__ == "__main__":
    app.run(debug=True)

