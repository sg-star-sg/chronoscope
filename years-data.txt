// Curated year-in-history dataset.
// Each event: { t: title, d: one-line description, c: category tag, l: read-more link }
// Categories: world, politics, war, science, culture, economy, disaster
const YEAR_DATA = {
1776: { headline: "A new republic declares itself", events: [
  { t: "Declaration of Independence", d: "The Second Continental Congress adopts the Declaration, formally announcing the thirteen American colonies' break from Britain.", c: "politics", l: "https://en.wikipedia.org/wiki/United_States_Declaration_of_Independence", dt: "07-04" },
  { t: "Battle of Trenton nears", d: "Washington's army, badly weakened, sets up the winter campaign that will turn the Revolutionary War's momentum.", c: "war", l: "https://en.wikipedia.org/wiki/Battle_of_Trenton" },
  { t: "Adam Smith publishes The Wealth of Nations", d: "The book lays the intellectual groundwork for modern economics and free-market theory.", c: "economy", l: "https://en.wikipedia.org/wiki/The_Wealth_of_Nations" }
]},
1789: { headline: "Revolution in France, a new government in America", events: [
  { t: "Storming of the Bastille", d: "Parisians storm the royal fortress-prison, igniting the French Revolution.", c: "politics", l: "https://en.wikipedia.org/wiki/Storming_of_the_Bastille", dt: "07-14" },
  { t: "George Washington becomes first U.S. President", d: "Washington is inaugurated, and the new U.S. Constitution's government begins operating.", c: "politics", l: "https://en.wikipedia.org/wiki/1789_United_States_presidential_election" },
  { t: "Declaration of the Rights of Man", d: "France's National Assembly adopts a founding statement of human and civil rights.", c: "politics", l: "https://en.wikipedia.org/wiki/Declaration_of_the_Rights_of_Man_and_of_the_Citizen" }
]},
1865: { headline: "A war ends, a president falls, an amendment passes", events: [
  { t: "American Civil War ends", d: "Confederate General Robert E. Lee surrenders at Appomattox Court House, effectively ending the war.", c: "war", l: "https://en.wikipedia.org/wiki/American_Civil_War", dt: "04-09" },
  { t: "13th Amendment abolishes slavery", d: "The U.S. Constitution is amended to abolish slavery nationwide.", c: "politics", l: "https://en.wikipedia.org/wiki/Thirteenth_Amendment_to_the_United_States_Constitution" },
  { t: "Assassination of Abraham Lincoln", d: "President Lincoln is shot by John Wilkes Booth days after the war's end and dies the next morning.", c: "politics", l: "https://en.wikipedia.org/wiki/Assassination_of_Abraham_Lincoln", dt: "04-14" }
]},
1914: { headline: "The First World War begins", events: [
  { t: "Assassination of Archduke Franz Ferdinand", d: "The heir to the Austro-Hungarian throne is assassinated in Sarajevo, triggering a diplomatic crisis.", c: "politics", l: "https://en.wikipedia.org/wiki/Assassination_of_Archduke_Franz_Ferdinand", dt: "06-28" },
  { t: "World War I erupts", d: "A tangle of alliances pulls Europe's great powers into a war that will last four years and reshape the globe.", c: "war", l: "https://en.wikipedia.org/wiki/World_War_I" },
  { t: "Panama Canal opens", d: "The canal connecting the Atlantic and Pacific opens to commercial traffic, transforming global shipping.", c: "world", l: "https://en.wikipedia.org/wiki/Panama_Canal" }
]},
1917: { headline: "Revolution in Russia, America enters the war", events: [
  { t: "Russian Revolution", d: "The Bolsheviks, led by Lenin, seize power in October, ending centuries of tsarist rule.", c: "politics", l: "https://en.wikipedia.org/wiki/Russian_Revolution", dt: "11-07" },
  { t: "United States enters World War I", d: "The U.S. declares war on Germany, shifting the balance of the conflict.", c: "war", l: "https://en.wikipedia.org/wiki/United_States_in_World_War_I" },
  { t: "Balfour Declaration", d: "Britain publicly supports \"a national home for the Jewish people\" in Palestine, with lasting geopolitical consequences.", c: "politics", l: "https://en.wikipedia.org/wiki/Balfour_Declaration" }
]},
1929: { headline: "The Wall Street Crash", events: [
  { t: "Wall Street Crash of 1929", d: "Stock prices collapse over \"Black Thursday\" and \"Black Tuesday,\" wiping out fortunes and triggering the Great Depression.", c: "economy", l: "https://en.wikipedia.org/wiki/Wall_Street_Crash_of_1929", dt: "10-29" },
  { t: "Museum of Modern Art opens in New York", d: "MoMA opens its doors, becoming a defining institution for modern art.", c: "culture", l: "https://en.wikipedia.org/wiki/Museum_of_Modern_Art" },
  { t: "First Academy Awards ceremony", d: "Hollywood holds its first Oscars ceremony, honoring films from 1927–28.", c: "culture", l: "https://en.wikipedia.org/wiki/1st_Academy_Awards" }
]},
1933: { headline: "Roosevelt's New Deal, Hitler's rise", events: [
  { t: "Adolf Hitler becomes Chancellor of Germany", d: "Hitler is appointed Chancellor, and the Nazi Party begins consolidating totalitarian power.", c: "politics", l: "https://en.wikipedia.org/wiki/Machtergreifung", dt: "01-30" },
  { t: "FDR launches the New Deal", d: "President Franklin D. Roosevelt begins a sweeping program of relief, recovery, and reform to fight the Depression.", c: "economy", l: "https://en.wikipedia.org/wiki/New_Deal" },
  { t: "Prohibition ends in the U.S.", d: "The 21st Amendment repeals nationwide Prohibition of alcohol.", c: "politics", l: "https://en.wikipedia.org/wiki/Twenty-first_Amendment_to_the_United_States_Constitution" }
]},
1939: { headline: "The Second World War begins", events: [
  { t: "Germany invades Poland", d: "Germany's invasion prompts Britain and France to declare war, beginning World War II in Europe.", c: "war", l: "https://en.wikipedia.org/wiki/Invasion_of_Poland", dt: "09-01" },
  { t: "Molotov–Ribbentrop Pact", d: "Germany and the Soviet Union sign a non-aggression pact secretly dividing Eastern Europe.", c: "politics", l: "https://en.wikipedia.org/wiki/Molotov%E2%80%93Ribbentrop_Pact" },
  { t: "Gone with the Wind premieres", d: "The epic film becomes one of the highest-grossing movies of all time.", c: "culture", l: "https://en.wikipedia.org/wiki/Gone_with_the_Wind_(film)" }
]},
1941: { headline: "Pearl Harbor draws in the United States", events: [
  { t: "Attack on Pearl Harbor", d: "Japan launches a surprise attack on the U.S. Pacific Fleet, bringing America into World War II.", c: "war", l: "https://en.wikipedia.org/wiki/Attack_on_Pearl_Harbor", dt: "12-07" },
  { t: "Germany invades the Soviet Union", d: "Operation Barbarossa opens the war's largest land campaign, with catastrophic casualties on both sides.", c: "war", l: "https://en.wikipedia.org/wiki/Operation_Barbarossa" },
  { t: "Atlantic Charter signed", d: "Roosevelt and Churchill outline shared postwar goals, foreshadowing the United Nations.", c: "politics", l: "https://en.wikipedia.org/wiki/Atlantic_Charter" }
]},
1945: { headline: "World War II ends, the atomic age begins", events: [
  { t: "Atomic bombings of Hiroshima and Nagasaki", d: "The U.S. drops atomic bombs on two Japanese cities, hastening Japan's surrender and opening the nuclear age.", c: "war", l: "https://en.wikipedia.org/wiki/Atomic_bombings_of_Hiroshima_and_Nagasaki", dt: "08-06" },
  { t: "World War II ends", d: "Germany surrenders in May and Japan in August/September, ending the deadliest conflict in history.", c: "war", l: "https://en.wikipedia.org/wiki/End_of_World_War_II_in_Europe" },
  { t: "United Nations founded", d: "Fifty nations sign the UN Charter in San Francisco, creating a new international body to prevent future wars.", c: "politics", l: "https://en.wikipedia.org/wiki/United_Nations" },
  { t: "Liberation of Nazi concentration camps", d: "Allied forces liberate camps including Auschwitz and Bergen-Belsen, revealing the full scope of the Holocaust.", c: "world", l: "https://en.wikipedia.org/wiki/The_Holocaust" }
]},
1947: { headline: "Independence and a new global divide", events: [
  { t: "India and Pakistan gain independence", d: "British India is partitioned into two independent nations amid mass displacement and violence.", c: "politics", l: "https://en.wikipedia.org/wiki/Partition_of_India", dt: "08-15" },
  { t: "Marshall Plan announced", d: "The U.S. proposes a massive aid program to rebuild war-torn Western Europe.", c: "economy", l: "https://en.wikipedia.org/wiki/Marshall_Plan" },
  { t: "Cold War tensions harden", d: "The Truman Doctrine commits the U.S. to containing Soviet influence, setting the Cold War's terms.", c: "politics", l: "https://en.wikipedia.org/wiki/Truman_Doctrine" }
]},
1949: { headline: "A divided Germany, a new China, NATO forms", events: [
  { t: "People's Republic of China founded", d: "Mao Zedong proclaims the People's Republic after the Communist victory in the Chinese Civil War.", c: "politics", l: "https://en.wikipedia.org/wiki/Proclamation_of_the_People%27s_Republic_of_China" },
  { t: "NATO is founded", d: "Twelve nations sign the North Atlantic Treaty, forming a collective-defense alliance against Soviet expansion.", c: "politics", l: "https://en.wikipedia.org/wiki/NATO" },
  { t: "Soviet Union tests its first atomic bomb", d: "The USSR ends the U.S. nuclear monopoly, accelerating the Cold War arms race.", c: "war", l: "https://en.wikipedia.org/wiki/RDS-1" }
]},
1950: { headline: "The Korean War begins", events: [
  { t: "Korean War begins", d: "North Korea invades South Korea, drawing in a UN coalition led by the United States.", c: "war", l: "https://en.wikipedia.org/wiki/Korean_War" },
  { t: "Peanuts comic strip debuts", d: "Charles Schulz's strip introduces Charlie Brown and Snoopy, becoming a cultural fixture.", c: "culture", l: "https://en.wikipedia.org/wiki/Peanuts" }
]},
1953: { headline: "Korea armistice, Everest summited, DNA's structure found", events: [
  { t: "Korean War armistice signed", d: "Fighting ends in an armistice that still divides the Korean peninsula today.", c: "war", l: "https://en.wikipedia.org/wiki/Korean_Armistice_Agreement" },
  { t: "Structure of DNA described", d: "James Watson and Francis Crick publish the double-helix structure of DNA.", c: "science", l: "https://en.wikipedia.org/wiki/DNA" },
  { t: "First ascent of Mount Everest", d: "Edmund Hillary and Tenzing Norgay become the first climbers confirmed to reach the summit.", c: "culture", l: "https://en.wikipedia.org/wiki/1953_British_Mount_Everest_expedition" }
]},
1957: { headline: "The Space Age begins", events: [
  { t: "Sputnik 1 launches", d: "The Soviet Union launches the first artificial satellite, starting the Space Race.", c: "science", l: "https://en.wikipedia.org/wiki/Sputnik_1" },
  { t: "Treaty of Rome signed", d: "Six European nations create the European Economic Community, a forerunner of the EU.", c: "politics", l: "https://en.wikipedia.org/wiki/Treaty_of_Rome" },
  { t: "Little Rock Nine integrate school", d: "Nine Black students integrate Little Rock Central High under federal troop protection, a landmark of the civil rights movement.", c: "world", l: "https://en.wikipedia.org/wiki/Little_Rock_Nine" }
]},
1961: { headline: "First man in space, a wall in Berlin", events: [
  { t: "Yuri Gagarin becomes the first human in space", d: "The Soviet cosmonaut orbits Earth aboard Vostok 1.", c: "science", l: "https://en.wikipedia.org/wiki/Vostok_1", dt: "04-12" },
  { t: "Berlin Wall built", d: "East Germany erects a wall dividing Berlin, a stark symbol of the Cold War.", c: "politics", l: "https://en.wikipedia.org/wiki/Berlin_Wall", dt: "08-13" },
  { t: "Bay of Pigs Invasion fails", d: "A CIA-backed attempt to overthrow Fidel Castro collapses within days.", c: "politics", l: "https://en.wikipedia.org/wiki/Bay_of_Pigs_Invasion" }
]},
1963: { headline: "A dream, and an assassination", events: [
  { t: "\"I Have a Dream\" speech", d: "Martin Luther King Jr. addresses the March on Washington, a defining moment of the civil rights movement.", c: "world", l: "https://en.wikipedia.org/wiki/I_Have_a_Dream", dt: "08-28" },
  { t: "Assassination of John F. Kennedy", d: "President Kennedy is shot and killed in Dallas, Texas, shocking the world.", c: "politics", l: "https://en.wikipedia.org/wiki/Assassination_of_John_F._Kennedy", dt: "11-22" }
]},
1964: { headline: "Civil rights become law", events: [
  { t: "Civil Rights Act of 1964 signed", d: "The landmark U.S. law outlaws discrimination based on race, color, religion, sex, or national origin.", c: "politics", l: "https://en.wikipedia.org/wiki/Civil_Rights_Act_of_1964" },
  { t: "Gulf of Tonkin incident", d: "A disputed naval clash leads Congress to authorize escalated U.S. involvement in Vietnam.", c: "war", l: "https://en.wikipedia.org/wiki/Gulf_of_Tonkin_incident" },
  { t: "Nelson Mandela sentenced to life imprisonment", d: "Mandela is convicted of sabotage in South Africa and begins 27 years in prison.", c: "politics", l: "https://en.wikipedia.org/wiki/Rivonia_Trial" }
]},
1968: { headline: "A year of assassinations and upheaval", events: [
  { t: "Assassination of Martin Luther King Jr.", d: "The civil rights leader is shot in Memphis, sparking unrest across American cities.", c: "world", l: "https://en.wikipedia.org/wiki/Assassination_of_Martin_Luther_King_Jr.", dt: "04-04" },
  { t: "Assassination of Robert F. Kennedy", d: "The presidential candidate is shot in Los Angeles just after winning the California primary.", c: "politics", l: "https://en.wikipedia.org/wiki/Assassination_of_Robert_F._Kennedy", dt: "06-05" },
  { t: "Tet Offensive", d: "A massive North Vietnamese and Viet Cong offensive shifts American public opinion on the Vietnam War.", c: "war", l: "https://en.wikipedia.org/wiki/Tet_Offensive" },
  { t: "Prague Spring crushed", d: "Soviet-led forces invade Czechoslovakia to halt liberalizing reforms.", c: "politics", l: "https://en.wikipedia.org/wiki/Prague_Spring" }
]},
1969: { headline: "One giant leap", events: [
  { t: "Apollo 11 Moon landing", d: "Neil Armstrong and Buzz Aldrin become the first humans to walk on the Moon.", c: "science", l: "https://en.wikipedia.org/wiki/Apollo_11", dt: "07-20" },
  { t: "Woodstock festival", d: "Half a million people gather for a landmark music festival in upstate New York.", c: "culture", l: "https://en.wikipedia.org/wiki/Woodstock" },
  { t: "ARPANET sends its first message", d: "The precursor to the internet transmits its first data between two university computers.", c: "science", l: "https://en.wikipedia.org/wiki/ARPANET" }
]},
1973: { headline: "Oil shock and a war's end", events: [
  { t: "1973 oil crisis", d: "An OPEC oil embargo quadruples prices, triggering global economic turmoil.", c: "economy", l: "https://en.wikipedia.org/wiki/1973_oil_crisis" },
  { t: "Paris Peace Accords end U.S. involvement in Vietnam", d: "The agreement leads to the withdrawal of American combat troops from Vietnam.", c: "war", l: "https://en.wikipedia.org/wiki/Paris_Peace_Accords" },
  { t: "Yom Kippur War", d: "Egypt and Syria launch a surprise attack on Israel, reshaping Middle East diplomacy.", c: "war", l: "https://en.wikipedia.org/wiki/Yom_Kippur_War" }
]},
1979: { headline: "Revolution in Iran, war in Afghanistan", events: [
  { t: "Iranian Revolution", d: "The Shah is overthrown and Ayatollah Khomeini establishes an Islamic Republic.", c: "politics", l: "https://en.wikipedia.org/wiki/Iranian_Revolution" },
  { t: "Iran hostage crisis begins", d: "Militants seize the U.S. embassy in Tehran, holding 52 Americans hostage for 444 days.", c: "politics", l: "https://en.wikipedia.org/wiki/Iran_hostage_crisis" },
  { t: "Soviet Union invades Afghanistan", d: "The USSR intervenes to prop up a communist government, beginning a decade-long war.", c: "war", l: "https://en.wikipedia.org/wiki/Soviet%E2%80%93Afghan_War" }
]},
1980: { headline: "Cold War chill, a new decade of technology", events: [
  { t: "1980 Summer Olympics boycotted", d: "The U.S. and dozens of allies boycott the Moscow Olympics over the Soviet invasion of Afghanistan.", c: "world", l: "https://en.wikipedia.org/wiki/1980_Summer_Olympics_boycott" },
  { t: "CNN launches", d: "Ted Turner's Cable News Network becomes the first 24-hour news channel.", c: "culture", l: "https://en.wikipedia.org/wiki/CNN" },
  { t: "Assassination of John Lennon", d: "The former Beatle is shot and killed outside his New York apartment.", c: "culture", l: "https://en.wikipedia.org/wiki/Death_of_John_Lennon" }
]},
1985: { headline: "Glasnost begins to reshape the Soviet Union", events: [
  { t: "Mikhail Gorbachev becomes Soviet leader", d: "Gorbachev launches glasnost and perestroika, reforms that will reshape and ultimately dissolve the USSR.", c: "politics", l: "https://en.wikipedia.org/wiki/Perestroika" },
  { t: "Live Aid concerts", d: "Simultaneous benefit concerts in London and Philadelphia raise funds for Ethiopian famine relief.", c: "culture", l: "https://en.wikipedia.org/wiki/Live_Aid" }
]},
1989: { headline: "The Berlin Wall falls", events: [
  { t: "Fall of the Berlin Wall", d: "East Germans breach the wall dividing Berlin, a symbolic end to the Cold War's division of Europe.", c: "politics", l: "https://en.wikipedia.org/wiki/Fall_of_the_Berlin_Wall", dt: "11-09" },
  { t: "Tiananmen Square protests", d: "Chinese troops violently suppress pro-democracy demonstrations in Beijing.", c: "politics", l: "https://en.wikipedia.org/wiki/1989_Tiananmen_Square_protests_and_massacre", dt: "06-04" },
  { t: "Exxon Valdez oil spill", d: "A tanker spill in Alaska's Prince William Sound becomes one of the worst environmental disasters in U.S. history.", c: "disaster", l: "https://en.wikipedia.org/wiki/Exxon_Valdez_oil_spill" }
]},
1991: { headline: "The Soviet Union dissolves", events: [
  { t: "Dissolution of the Soviet Union", d: "The USSR formally breaks apart into fifteen independent states, ending the Cold War era.", c: "politics", l: "https://en.wikipedia.org/wiki/Dissolution_of_the_Soviet_Union", dt: "12-26" },
  { t: "Gulf War", d: "A U.S.-led coalition expels Iraqi forces from Kuwait in Operation Desert Storm.", c: "war", l: "https://en.wikipedia.org/wiki/Gulf_War" },
  { t: "World Wide Web goes public", d: "Tim Berners-Lee's World Wide Web becomes publicly available, laying the foundation for the modern internet.", c: "science", l: "https://en.wikipedia.org/wiki/World_Wide_Web" }
]},
1994: { headline: "Genocide in Rwanda, freedom for Mandela", events: [
  { t: "Rwandan genocide", d: "Roughly 800,000 Tutsi and moderate Hutu are killed over about 100 days.", c: "world", l: "https://en.wikipedia.org/wiki/Rwandan_genocide" },
  { t: "Nelson Mandela elected President of South Africa", d: "Mandela becomes South Africa's first Black president in the country's first fully democratic election.", c: "politics", l: "https://en.wikipedia.org/wiki/1994_South_African_general_election" },
  { t: "North American Free Trade Agreement (NAFTA) takes effect", d: "The trade pact between the U.S., Canada, and Mexico eliminates most tariffs between the three countries.", c: "economy", l: "https://en.wikipedia.org/wiki/North_American_Free_Trade_Agreement" }
]},
1997: { headline: "Hong Kong returns, a princess dies", events: [
  { t: "Handover of Hong Kong", d: "Britain transfers sovereignty of Hong Kong to China after over 150 years of colonial rule.", c: "politics", l: "https://en.wikipedia.org/wiki/Transfer_of_the_sovereignty_of_Hong_Kong" },
  { t: "Death of Diana, Princess of Wales", d: "Diana dies in a car crash in Paris, prompting an outpouring of global mourning.", c: "culture", l: "https://en.wikipedia.org/wiki/Death_of_Diana,_Princess_of_Wales" },
  { t: "Asian financial crisis", d: "Currency collapses spread across Southeast Asia, triggering a broader financial crisis.", c: "economy", l: "https://en.wikipedia.org/wiki/1997_Asian_financial_crisis" }
]},
2000: { headline: "Y2K and a contested U.S. election", events: [
  { t: "Y2K arrives without major disruption", d: "Feared computer failures from the year-2000 date rollover largely fail to materialize after years of remediation work.", c: "science", l: "https://en.wikipedia.org/wiki/Year_2000_problem" },
  { t: "Dot-com bubble begins to burst", d: "The Nasdaq peaks in March before a two-year collapse in internet-company valuations begins.", c: "economy", l: "https://en.wikipedia.org/wiki/Dot-com_bubble" },
  { t: "Bush v. Gore", d: "A disputed U.S. presidential election is ultimately decided by the Supreme Court.", c: "politics", l: "https://en.wikipedia.org/wiki/2000_United_States_presidential_election" }
]},
2001: { headline: "September 11", events: [
  { t: "September 11 attacks", d: "Al-Qaeda hijackers crash planes into the World Trade Center and the Pentagon, killing nearly 3,000 people.", c: "world", l: "https://en.wikipedia.org/wiki/September_11_attacks", dt: "09-11" },
  { t: "War in Afghanistan begins", d: "The U.S. and allies invade Afghanistan to oust the Taliban and pursue al-Qaeda.", c: "war", l: "https://en.wikipedia.org/wiki/War_in_Afghanistan_(2001%E2%80%932021)" },
  { t: "Wikipedia launches", d: "The free, collaboratively edited encyclopedia goes online.", c: "culture", l: "https://en.wikipedia.org/wiki/Wikipedia" }
]},
2003: { headline: "Invasion of Iraq", events: [
  { t: "U.S.-led invasion of Iraq", d: "A coalition led by the U.S. invades Iraq and topples Saddam Hussein, citing unfounded claims of weapons of mass destruction.", c: "war", l: "https://en.wikipedia.org/wiki/2003_invasion_of_Iraq" },
  { t: "Space Shuttle Columbia disaster", d: "The shuttle disintegrates on re-entry, killing all seven crew members.", c: "disaster", l: "https://en.wikipedia.org/wiki/Space_Shuttle_Columbia_disaster" },
  { t: "SARS outbreak", d: "A novel coronavirus causes a global outbreak, foreshadowing later pandemic response challenges.", c: "science", l: "https://en.wikipedia.org/wiki/2002%E2%80%932004_SARS_outbreak" }
]},
2004: { headline: "A devastating tsunami, social media begins", events: [
  { t: "Indian Ocean earthquake and tsunami", d: "A magnitude-9.1 earthquake triggers a tsunami that kills over 225,000 people across a dozen countries.", c: "disaster", l: "https://en.wikipedia.org/wiki/2004_Indian_Ocean_earthquake_and_tsunami" },
  { t: "Facebook launches", d: "Mark Zuckerberg launches Facebook from a Harvard dorm room, eventually reshaping global social media.", c: "culture", l: "https://en.wikipedia.org/wiki/Facebook" }
]},
2008: { headline: "The global financial crisis", events: [
  { t: "Global financial crisis / Great Recession", d: "The collapse of Lehman Brothers and the U.S. housing bubble triggers the worst financial crisis since the Great Depression.", c: "economy", l: "https://en.wikipedia.org/wiki/Great_Recession", dt: "09-15" },
  { t: "Barack Obama elected", d: "Obama becomes the first Black president of the United States.", c: "politics", l: "https://en.wikipedia.org/wiki/2008_United_States_presidential_election", dt: "11-04" },
  { t: "Beijing hosts the Summer Olympics", d: "China stages a lavish Olympic Games, signaling its arrival as a global power.", c: "world", l: "https://en.wikipedia.org/wiki/2008_Summer_Olympics" }
]},
2010: { headline: "The Arab Spring's spark", events: [
  { t: "Arab Spring begins", d: "A Tunisian street vendor's self-immolation sets off a wave of uprisings across the Arab world.", c: "politics", l: "https://en.wikipedia.org/wiki/Arab_Spring" },
  { t: "Deepwater Horizon oil spill", d: "An explosion on a BP drilling rig causes the largest marine oil spill in history in the Gulf of Mexico.", c: "disaster", l: "https://en.wikipedia.org/wiki/Deepwater_Horizon_oil_spill" },
  { t: "Haiti earthquake", d: "A magnitude-7.0 earthquake devastates Haiti, killing over 100,000 people.", c: "disaster", l: "https://en.wikipedia.org/wiki/2010_Haiti_earthquake" }
]},
2011: { headline: "Bin Laden killed, an uprising topples regimes", events: [
  { t: "Death of Osama bin Laden", d: "U.S. Navy SEALs kill the al-Qaeda leader in a raid in Pakistan.", c: "war", l: "https://en.wikipedia.org/wiki/Death_of_Osama_bin_Laden", dt: "05-02" },
  { t: "Fukushima nuclear disaster", d: "A tsunami triggers meltdowns at Japan's Fukushima Daiichi plant, the worst nuclear accident since Chernobyl.", c: "disaster", l: "https://en.wikipedia.org/wiki/Fukushima_nuclear_accident" },
  { t: "Arab Spring topples leaders", d: "Longtime rulers in Tunisia, Egypt, and Libya are ousted amid mass protests and civil conflict.", c: "politics", l: "https://en.wikipedia.org/wiki/Arab_Spring" }
]},
2012: { headline: "A war in Syria deepens", events: [
  { t: "Syrian Civil War escalates", d: "Protests against Bashar al-Assad's government spiral into a full civil war that will displace millions.", c: "war", l: "https://en.wikipedia.org/wiki/Syrian_civil_war" },
  { t: "Hurricane Sandy", d: "One of the costliest Atlantic hurricanes on record devastates the U.S. Northeast Caribbean.", c: "disaster", l: "https://en.wikipedia.org/wiki/Hurricane_Sandy" },
  { t: "Curiosity rover lands on Mars", d: "NASA's rover touches down to begin its search for signs of past habitability.", c: "science", l: "https://en.wikipedia.org/wiki/Curiosity_(rover)" }
]},
2014: { headline: "Russia annexes Crimea", events: [
  { t: "Annexation of Crimea", d: "Russia annexes Ukraine's Crimean peninsula following a disputed referendum, drawing international condemnation.", c: "war", l: "https://en.wikipedia.org/wiki/Annexation_of_Crimea_by_the_Russian_Federation" },
  { t: "West African Ebola epidemic", d: "The largest Ebola outbreak in history kills over 11,000 people, mostly in Guinea, Liberia, and Sierra Leone.", c: "disaster", l: "https://en.wikipedia.org/wiki/Western_African_Ebola_virus_epidemic" },
  { t: "Islamic State declares a caliphate", d: "ISIS seizes large parts of Iraq and Syria, prompting a renewed international military response.", c: "war", l: "https://en.wikipedia.org/wiki/Islamic_State" }
]},
2015: { headline: "Paris climate accord, a migrant crisis", events: [
  { t: "Paris Agreement adopted", d: "Nearly 200 countries agree to a landmark global framework to limit climate change.", c: "world", l: "https://en.wikipedia.org/wiki/Paris_Agreement" },
  { t: "European migrant crisis peaks", d: "Over a million people, many fleeing the Syrian war, seek asylum in Europe.", c: "world", l: "https://en.wikipedia.org/wiki/European_migrant_crisis" },
  { t: "Same-sex marriage legalized nationwide in the U.S.", d: "The Supreme Court's Obergefell v. Hodges ruling legalizes same-sex marriage across the country.", c: "politics", l: "https://en.wikipedia.org/wiki/Obergefell_v._Hodges" }
]},
2016: { headline: "Brexit and a stunning U.S. election", events: [
  { t: "Brexit referendum", d: "The UK votes to leave the European Union in a referendum that reshapes British politics for years.", c: "politics", l: "https://en.wikipedia.org/wiki/2016_United_Kingdom_European_Union_membership_referendum", dt: "06-23" },
  { t: "Donald Trump elected U.S. President", d: "Trump wins the presidency in an upset over Hillary Clinton.", c: "politics", l: "https://en.wikipedia.org/wiki/2016_United_States_presidential_election", dt: "11-08" },
  { t: "Gravitational waves detected", d: "Scientists announce the first direct detection of gravitational waves, confirming a key prediction of Einstein's relativity.", c: "science", l: "https://en.wikipedia.org/wiki/First_observation_of_gravitational_waves" }
]},
2019: { headline: "A novel virus emerges", events: [
  { t: "First COVID-19 cases identified", d: "A cluster of unexplained pneumonia cases in Wuhan, China, is later identified as the start of the COVID-19 pandemic.", c: "world", l: "https://en.wikipedia.org/wiki/COVID-19_pandemic" },
  { t: "First image of a black hole released", d: "The Event Horizon Telescope collaboration releases humanity's first direct image of a black hole.", c: "science", l: "https://en.wikipedia.org/wiki/Event_Horizon_Telescope" },
  { t: "Notre-Dame de Paris fire", d: "A fire severely damages the historic Notre-Dame Cathedral, destroying its spire and roof.", c: "disaster", l: "https://en.wikipedia.org/wiki/Notre-Dame_de_Paris_fire" }
]},
2020: { headline: "The COVID-19 pandemic", events: [
  { t: "COVID-19 declared a global pandemic", d: "The WHO declares a pandemic as the virus spreads worldwide, triggering lockdowns and over 7 million eventual deaths.", c: "world", l: "https://en.wikipedia.org/wiki/COVID-19_pandemic", dt: "03-11" },
  { t: "George Floyd's murder sparks global protests", d: "The killing of George Floyd by Minneapolis police ignites worldwide protests against racial injustice.", c: "world", l: "https://en.wikipedia.org/wiki/Murder_of_George_Floyd" },
  { t: "Joe Biden elected U.S. President", d: "Biden defeats incumbent Donald Trump in a high-turnout election held amid the pandemic.", c: "politics", l: "https://en.wikipedia.org/wiki/2020_United_States_presidential_election" },
  { t: "First mRNA COVID-19 vaccines authorized", d: "Pfizer-BioNTech and Moderna vaccines receive emergency authorization within a year of the virus's emergence.", c: "science", l: "https://en.wikipedia.org/wiki/COVID-19_vaccine" }
]},
2021: { headline: "An insurrection, a chaotic withdrawal", events: [
  { t: "January 6 U.S. Capitol attack", d: "A mob of Trump supporters storms the U.S. Capitol to disrupt certification of the 2020 election.", c: "politics", l: "https://en.wikipedia.org/wiki/January_6_United_States_Capitol_attack" },
  { t: "Fall of Kabul", d: "The Taliban retake Afghanistan as U.S. forces withdraw after 20 years of war.", c: "war", l: "https://en.wikipedia.org/wiki/2021_Taliban_offensive" },
  { t: "Suez Canal blocked", d: "The container ship Ever Given runs aground, blocking the canal for six days and disrupting global trade.", c: "economy", l: "https://en.wikipedia.org/wiki/Obstruction_of_the_Suez_Canal_by_Ever_Given" }
]},
2022: { headline: "Russia invades Ukraine", events: [
  { t: "Russian invasion of Ukraine", d: "Russia launches a full-scale invasion of Ukraine, triggering Europe's largest war since 1945 and a global energy crisis.", c: "war", l: "https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine", dt: "02-24" },
  { t: "ChatGPT launches", d: "OpenAI releases ChatGPT, sparking a wave of mainstream interest in generative AI.", c: "science", l: "https://en.wikipedia.org/wiki/ChatGPT" },
  { t: "Queen Elizabeth II dies", d: "Britain's longest-reigning monarch dies after 70 years on the throne; Charles III becomes king.", c: "world", l: "https://en.wikipedia.org/wiki/Death_and_state_funeral_of_Elizabeth_II" }
]},
2023: { headline: "War breaks out in the Middle East", events: [
  { t: "Hamas attack on Israel and Gaza war", d: "A Hamas-led attack on Israel kills roughly 1,200 people, triggering a devastating war in Gaza.", c: "war", l: "https://en.wikipedia.org/wiki/Gaza_war" },
  { t: "Turkey–Syria earthquakes", d: "A magnitude-7.8 earthquake kills over 55,000 people across southern Turkey and northern Syria.", c: "disaster", l: "https://en.wikipedia.org/wiki/2023_Turkey%E2%80%93Syria_earthquakes" },
  { t: "Generative AI boom accelerates", d: "Major tech companies race to release competing large language models and AI tools through the year.", c: "science", l: "https://en.wikipedia.org/wiki/Generative_artificial_intelligence" }
]},
2024: { headline: "Elections around the world", events: [
  { t: "\"Super election year\"", d: "Over 60 countries, including the U.S., India, and the UK, hold major national elections in the same year.", c: "politics", l: "https://en.wikipedia.org/wiki/2024_in_politics" },
  { t: "Donald Trump re-elected U.S. President", d: "Trump defeats Kamala Harris to win a second, non-consecutive presidential term.", c: "politics", l: "https://en.wikipedia.org/wiki/2024_United_States_presidential_election" },
  { t: "Assad regime falls in Syria", d: "Rebel forces topple Bashar al-Assad's government in a rapid offensive, ending over 50 years of family rule.", c: "war", l: "https://en.wikipedia.org/wiki/Fall_of_the_Assad_regime" }
]},
2025: { headline: "A fragile ceasefire, an AI arms race", events: [
  { t: "Gaza ceasefire and hostage deal", d: "Israel and Hamas reach a ceasefire and phased hostage-release agreement after over a year of war.", c: "war", l: "https://en.wikipedia.org/wiki/Gaza_war" },
  { t: "Trump returns to office", d: "Donald Trump is inaugurated for a second term, reshaping U.S. trade, immigration, and foreign policy.", c: "politics", l: "https://en.wikipedia.org/wiki/Second_presidency_of_Donald_Trump" },
  { t: "AI investment boom continues", d: "Frontier AI labs and chipmakers see massive valuations and capital spending amid an intensifying race for advanced AI.", c: "economy", l: "https://en.wikipedia.org/wiki/2025_in_artificial_intelligence" }
]}
};
