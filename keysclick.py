import json
txt='[["00601047", "Gurung,Vinita", "GURUNG", "VINITA", "2021-09-20 00:00:00"], ["00601048", "Janik,Chantal", "JANIK", "CHANTAL", "2021-09-28 00:00:00"], ["00601049", "Al-Mamoori,Warood", "ALMAMOORI", "WAROOD", "2021-09-28 00:00:00"], ["00601050", "Martin,Khalil", "MARTIN", "KHALIL", "2021-09-28 00:00:00"], ["00601051", "Smith,Ezra", "SMITH", "EZRA", "2021-09-28 00:00:00"], ["00601052", "Lovell,Elizabeth", "LOVELL", "ELIZABETH", "2021-09-28 00:00:00"], ["00601053", "Boudreau,Olivia", "BOUDREAU", "OLIVIA", "2021-09-29 00:00:00"], ["00601054", "Rainville,Keely", "RAINVILLE", "KEELY", "2021-09-29 00:00:00"], ["00601055", "Gagnon,Julie", "GAGNON", "JULIE", "2021-09-26 00:00:00"], ["00601056", "Caputo,Mikaela", "CAPUTO", "MIKAELA", "2021-09-27 00:00:00"], ["00601057", "Khando,Tsering", "KHANDO", "TSERING", "2021-09-26 00:00:00"], ["00601058", "Danailovski,Marko", "DANAILOVSKI", "MARKO", "2021-09-26 00:00:00"], ["00601059", "Prymicz,Dominik", "PRYMICZ", "DOMINIK", "2021-09-29 00:00:00"], ["00601060", "Marques,Felipe", "MARQUES", "FELIPE", "2021-10-01 00:00:00"], ["00601061", "Panchal,Vaibhavi Sureshkumar", "PANCHAL", "VAIBHAVI", "2021-10-01 00:00:00"], ["00601062", "Maldonado,Estefanny", "MALDONADO", "ESTEFANNY", "2021-10-01 00:00:00"], ["00601063", "LaFleur,Courtney", "LAFLEUR", "COURTNEY", "2021-10-02 00:00:00"], ["00601064", "Chambueta,Ivan", "CHAMBUETA", "IVAN", "2021-10-04 00:00:00"], ["00601065", "Coleto,Rafael", "COLETO", "RAFAEL", "2021-10-04 00:00:00"], ["00601066", "Vilar,Nicolas Batista", "VILAR", "NICOLAS", "2021-10-04 00:00:00"], ["00601067", "Dagala,Maria Andrea Nicole", "DAGALA", "MARIA", "2021-10-04 00:00:00"], ["00601068", "Zigman,Mitchell", "ZIGMAN", "MITCHELL", "2021-10-04 00:00:00"], ["00601069", "Jensen,Melissa", "JENSEN", "MELISSA", "2021-10-04 00:00:00"], ["00601070", "Snow,Cassondra", "SNOW", "CASSONDRA", "2021-10-04 00:00:00"], ["00601071", "Leung,Liam", "LEUNG", "LIAM", "2021-10-04 00:00:00"], ["00601072", "Rodriguez Rios,Melissa", "RODRIGUEZRIOS", "MELISSA", "2021-10-04 00:00:00"], ["00601073", "Lidstone,Kaleb", "LIDSTONE", "KALEB", "2021-10-04 00:00:00"], ["00601074", "Girardi,Martin", "GIRARDI", "MARTIN", "2021-10-07 00:00:00"], ["00601075", "Gonzales,Kaye Marie", "GONZALES", "KAYE", "2021-10-07 00:00:00"], ["00601076", "Morier,Erica", "MORIER", "ERICA", "2021-09-30 00:00:00"], ["00601077", "O Boyle,Erin", "OBOYLE", "ERIN", "2021-09-30 00:00:00"], ["00601078", "King,Michael", "KING", "MICHAEL", "2021-10-14 00:00:00"], ["00601079", "Stephen,Esther", "STEPHEN", "ESTHER", "2021-10-14 00:00:00"], ["00601080", "Vallado Pacheco,Roberto", "VALLADOPACHECO", "ROBERTO", "2021-10-15 00:00:00"], ["00601081", "Henderson,Justin", "HENDERSON", "JUSTIN", "2021-10-15 00:00:00"], ["00601082", "Clement,Deanna", "CLEMENT", "DEANNA", "2021-10-18 00:00:00"], ["00601083", "Birch,Mandy", "BIRCH", "MANDY", "2021-10-17 00:00:00"], ["00601084", "Lamothe,Christiana", "LAMOTHE", "CHRISTIANA", "2021-10-15 00:00:00"], ["00601085", "Vo,Nguyen Kim Han", "VO", "NGUYENKIMHAN", "2021-10-15 00:00:00"], ["00601087", "Kovacs,Bronson", "KOVACS", "BRONSON", "2021-10-22 00:00:00"], ["00601088", "Vanderleest,William", "VANDERLEEST", "WILLIAM", "2021-09-01 00:00:00"], ["00601089", "Avilla,Jayda", "AVILLA", "JAYDA", "2021-10-24 00:00:00"], ["00601090", "Alvarez,Glacel Marie Manubag", "ALVAREZ", "GLACELMARIEMANUBAG", "2021-10-24 00:00:00"], ["00601091", "Bonnema,Jessica L.", "BONNEMA", "JESSICA", "2021-10-21 00:00:00"], ["00601092", "Flores Rodriguez,Ruth Giulianna", "FLORESRODRIGUEZ", "RUTHGIULIANNA", "2021-10-10 00:00:00"], ["00601093", "Acosta Alvarez,Paty", "ACOSTAALVAREZ", "PATY", "2021-11-01 00:00:00"], ["00601094", "Tandoc,Xylene", "TANDOC", "XYLENE", "2021-11-01 00:00:00"], ["00601095", "Lama,Rashmi", "LAMA", "RASHMI", "2021-11-01 00:00:00"], ["00601096", "Booth,Hannah", "BOOTH", "HANNAH", "2021-11-02 00:00:00"], ["00601097", "DiPasquale,Sara", "DIPASQUALE", "SARA", "2021-11-02 00:00:00"], ["00601098", "Bascoe,Rushawn", "BASCOE", "RUSHAWN", "2021-11-05 00:00:00"], ["00601099", "Lo,Priscilla Yee-Lam", "LO", "PRISCILLA", "2021-10-10 00:00:00"]]'

