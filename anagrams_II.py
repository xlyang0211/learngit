__author__ = 'seany'

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        if len(strs) < 2:
            return []
        ret = []
        flag_list = [False] * len(strs)
        for i in xrange(len(strs)):
            if flag_list[i]:
                pass
            else:
                lst = [strs[i]]
                for j in xrange(i+1, len(strs)):
                    if flag_list[i]:
                        pass
                    else:
                        if sorted(strs[i]) == sorted(strs[j]):
                            flag_list[j] = True
                            lst.append(strs[j])
                if len(lst) > 1:
                    ret.append(lst)
        return ret

if __name__ == "__main__":
    solution = Solution()
    strs = ["ate", "treat", "eat", "tea", "ttrea", "hello"]
    strs = ["multiplying","flamboyantly","profession","loft","voluntary","fudges","swore","flanks","diet","pamphlets","dispatchers","afterbirths","boutiques","motifs","massenet","translator","cup","mountbatten","constipated","monotonically","stability","reenact","pols","bowed","berthed","wreathing","ecclesiastes","stylistically","chandigarh","carpenters","freestyle","reflexively","palimpsest","ampul","deliberates","reactor","metals","deforests","coloring","guadalajara","ra","natural","creepies","dankly","disqualifies","hometowns","disengages","papergirls","phrenology","receptors","concessions","judgements","hummocked","whiner","repaying","selvaged","wattest","throats","persecutor","seagram","akimbo","bureaucratically","stepbrothers","transubstantiation","enjoy","couping","rhizome","paramount","raccoon","hafiz","admiration","snakebite","rumors","lasting","ammo","acquirable","harvard","monomaniac","tonnages","rakish","doses","beneficently","essential","statistically","consultancies","cliffs","ringleaders","effusively","condescension","lime","helplessness","jerking","schemers","glosses","grinding","bacterial","stone","disintegrate","enormous","miniaturized","impetuous","nude","fumbles","corpora","beneficiaries","powerlessly","judgment","doctorates","decade","gracelessly","pollard","sangfroid","overspecialized","mews","repaired","islamics","stinks","jasmine","formulate","chloride","septembers","congress","scrap","threshed","mechanizing","egotist","bicepses","grabs","pudding","mariachis","kong","canonicals","bumpiest","mossiest","obsessing","floral","deed","baron","rubbishes","refuting","remainder","woodsier","kapok","instruments","matriculated","cub","marched","librettos","splendor","wyo","silkworm","llewellyn","anesthesia","nagged","wellsprings","stationing","airedale","axed","decors","smug","sucking","humanoid","backside","sacramento","swinburne","sirups","oakum","fumigating","valarie","flotilla","crevices","surmountable","inquiringly","spotters","ferrets","bulldoze","combatant","shane","satiny","camshafts","carped","published","crooners","imperceptible","dispatches","examples","earmuffs","gramme","lung","plied","fallowing","liberties","cratered","mauling","patronizes","flaked","inspects","cusp","wakened","outbalanced","speckled","compose","oleaginous","heiresses","cashiers","ark","premises","narrowness","computations","mongolism","steamy","informant","dice","compounded","acrylic","scrunch","penlight","imputations","clerics","dressmakers","dangers","paying","tunes","murkiest","effusive","misanthropist","alloying","terrorize","costner","virginian","pampering","sufficient","incisors","culotte","gusting","relapsed","headstrong","backspaced","engaged","strikingly","schemed","diversifying","hyper","accountant","nosegay","occluded","underarm","cyclically","amuck","cutlet","perpetrators","malfeasance","pompey","monolingual","cutthroats","hails","delimit","grudging","heraldic","doc","melanges","alerted","disappearance","sharpe","livers","shoemaker","wealthiness","antipersonnel","serbia","guzzled","dmitri","threshes","skyrocketed","ionized","amend","grotesques","containers","platonism","tabbies","lames","infatuation","locus","acquaintance","mouthfuls","coroners","glands","bilges","queasy","dewitt","pidgin","bicentennial","radish","unlawfully","junketed","use","negotiate","hailing","typo","sanity","mallard","incubating","typed","midterm","glacially","maestro","reincarnate","transpiring","strolling","verbena","trapper","flyers","helmsman","mischievous","pendants","rosalie","beatles","carpals","crinkling","recapped","command","rolando","union","bert","hera","mimeographing","vulgarly","pertinacious","markham","borodin","malevolence","resuscitating","interrelationship","indulging","earthling","wishers","bludgeoned","canvassed","canute","microsoft","bikes","hialeah","mountains","physicals","overstepped","cornstalks","temperament","patriots","irreverently","blitz","firewall","sharpshooter","fizzing","handicappers","ultrasonic","halftime","mcnamara","bratislava","clink","anaesthetized","desmond","vaccines","ed","peccaries","mantillas","indemnifications","retypes","scenarios","regressed","sauced","wins","kresge","sparkled","miseries","reformed","moss","tethers","outsizes","contests","funner","wagons","shortness","drivers","estate","coquettish","favorites","watersides","egos","foiling","dismaying","obligating","lit","fiord","s","cautioning","ararat","creditable","caerphilly","tinkers","arrayed","transgressions","temperas","cantaloup","suffragettes","impacts","workplaces","hostlers","feebly","regular","tarring","vetoes","snack","signifying","frisk","diacritic","thea","spirally","floodlit","minibike","concepts","sustain","dissociated","vassaling","credenza","adjacent","blithe","culture","languors","bunker","bucked","pulsar","chromosome","vicky","viewfinders","accosts","nominal","kshatriya","reamer","amorous","signify","nuttiest","tomlin","resume","greatest","learners","brashness","plaiting","feminists","oddness","facelifts","seaport","interdicting","renewed","reprogrammed","smoulder","bernhardt","wangled","choir","listens","crusty","heavenward","failures","per","proctors","edifice","trespassing","displeased","fuddle","partner","motor","editorialize","fishbowls","rangier","chats","wreckage","covet","guzzlers","scapegoats","silicates","szymborska","biplanes","necktie","optic","macao","hyped","medications","nemesis","mandates","splodge","resins","angelica","gaffed","atavistic","petioles","anxiety","killjoys","misuses","nabobs","queens","conceivably","castling","haltingly","serapes","whizz","punctuating","seaweed","eunuchs","bidets","midpoints","breaded","flunky","tithe","urbanized","balcony","winked","goldener","robotics","manichean","garrison","rattles","songbirds","haldane","bankrupting","whitehall","questioningly","gofers","perfection","ghostwriting","mosley","swimmer","soliloquizing","freeholder","draining","outfoxed","flanneling","biggest","licked","trendier","impoverishing","commits","advisement","unclasping","basking","rico","cagiest","auspicious","legislate","trevor","chevrons","proceeds","steward","bloating","resourcefully","anodynes","gallivant","modifier","mugs","verizon","kip","potties","blaine","thud","chastest","hibernate","pastor","rovers","schmaltz","discomfited","prefabricating","cruisers","mutts","sputtered","doable","sheik","laocoon","politicize","wretcheder","rankling","sides","docs","gluing","pickaxed","pedagogical","describe","spec","toni","unimaginative","guidance","distorter","congeniality","harvests","daniel","irrigates","mallomars","sevenths","decisive","stylish","angleworm","dido","conventing","roweling","zing","relish","prearrange","atheistic","goldsmiths","setbacks","topcoat","condoled","compensate","heavenly","voyeurs","judases","shortchanging","trooped","badmouths","requites","immigrating","opticians","swellheads","sated","cannibalizes","continental","frothed","curios","unlike","replications","cormorants","scaramouch","thingamajig","plunged","ainu","bilbao","glops","shoplifting","basses","clark","nerving","bosom","cruciform","throttle","pokey","envelope","medicaid","indifferent","fluency","echelons","espying","twirlers","cathryn","concluding","punctilious","churchgoers","comparing","persimmons","ducal","flatt","wearer","mandarin","iphigenia","rub","playrooms","lorrie","carries","incapacitates","earn","electrified","adrenal","marcher","phrases","antibiotic","eventually","balconies","carton","toggle","molded","protrusions","croquettes","outwears","reciprocals","poisons","homogenized","sufi","tartuffe","retractable","schoolhouses","megaliths","transliteration","surreys","awaited","wetted","participial","subsidized","anticipates","capulet","equate","observable","excrescences","oceanographers","devise","beds","tolling","quilts","hierarchical","cloches","relative","blossoming","woodsheds","at","stilling","spacial","sublet","doggoning","vermilion","rhiannon","yangon","strictest","podding","hittite","stiffened","suited","admonitions","occupational","regulation","fetter","panelists","chillers","irma","aspirant","ayyubid","exceptionable","drunken","tread","carpel","vests","countered","aeroflot","assigned","exhorted","attentions","euclidean","cellars","anons","exhausting","body","clattering","numbered","battled","ventilate","sculptured","imelda","solemner","unimpaired","sequesters","preachier","gums","malignantly","luftwaffe","intact","reinforcement","misses","durante","calculates","susanne","compass","beryls","filibuster","entailing","eclectically","shivers","letting","inflammations","asseverating","psychos","cyrus","hoop","wondrous","ritual","photogenic","josue","magnifier","spitted","theorize","notebooks","pacing","proportions","secretary","cavity","scampering","recline","snyder","sugariest","rowdiest","discommodes","rory","arteries","outranks","inflect","latticework","abusive","gaslights","cactuses","overreaches","mushiest","lagrange","sciatica","bulging","apse","lucked","burying","annoyed","sub","thoroughfares","offshore","villa","vermont","akron","rep","stutterer","stendhal","redeemer","research","lithium","sprucer","unavailing","bulldozer","herringboned","misapply","gybes","frobisher","snippier","career","rhymes","bolivar","esq","alison","backers","motleyest","toots","infelicitous","swaying","telecommunication","reproves","tersely","joyriding","snuffles","crick","jut","preppies","testifies","retooling","grandstands","riveted","dillydally","flute","procreate","peppier","decorating","alcoholics","langland","cohort","eroded","sonnets","consent","jackrabbits","spadework","lunchboxes","anesthesiology","stubbornest","quixotism","ambidextrously","return","stockbroker","aqueduct","fluent","praises","bemoans","missourians","firths","bluenoses","sprained","workbooks","wobblier","bereavement","institutionalizing","shindig","subtitled","knifing","acrylics","cortez","muled","infer","integrates","grid","sentimentalizing","liberia","flamethrower","entity","detoxify","copra","meridians","milieus","atrium","grays","resultants","mincemeat","concentrates","viscountesses","connoting","jerkily","tiger","engendered","spectacular","fritter","billions","puers","wormwood","genuine","sticking","monograph","wander","evacuated","bargained","syphilitics","logging","model","entrapped","tirade","blondie","windmills","incompetent","battlegrounds","leaden","conjectures","testimonials","soil","downcast","polio","remounted","rekindle","disingenuous","paternalistic","adobes","bibliophile","sindbad","gizmo","booing","thoughtlessness","tennis","skillets","woefullest","exult","briggs","womanize","wenches","radiate","hiccups","alexandra","hammer","indicator","hensley","adulteress","tiptoes","urologists","peters","endorse","repulses","squealed","adjudicating","swift","notionally","everything","flown","rediscovered","spinner","lividly","lyra","storeroom","hallelujahs","term","stabbings","wite","corrine","usefully","masters","subhead","gallantry","mercuries","navy","cristina","pray","salamander","asters","purgatory","recidivists","cognac","springsteen","multitude","wilberforce","drizzling","ramification"]
    strs = ["bluffed","excellently","neurology","nonrefillable","edmund","boyhoods","survivors","sexually","outnumbering","bolero","werewolf","debasing","dragnet","addams","monochromes","flippancy","hoots","digestion","profanity","cellist","enrols","crumble","elderberry","jayson","recopying","threats","exploded","cinnamon","hospitalized","ducat","memorialize","powerlessly","suaver","deservings","genuinely","calliope","oxidize","gamekeeper","slimming","daises","resisted","shanty","receivable","careering","transmigration","dooms","revisiting","financed","severs","hominy","pantomiming","bestride","seam","alibi","churchman","ovule","jaxartes","retirement","translated","pancaking","achiever","navigates","hazes","tubman","versatility","fergus","adjust","narcosis","hightail","mormon","hattie","chinning","teenager","tho","misbehaves","trustfulness","electioneers","emending","disenchanting","barometer","styluses","uruguay","houseboat","rungs","endwise","reinterpretation","gashes","koshers","nostalgic","hateful","bray","sutures","saudis","sentimentalizes","ayers","avoided","spiky","circumnavigated","tonic","dialects","disbursing","manitoba","potbellies","cauldron","whitened","fitter","attorney","doorbell","scrolled","noncontagious","overnight","rubbishes","stove","amortizing","periling","doublet","celina","whitfield","tonsures","overturns","missions","casuals","juxtaposing","sings","hesperus","panhandle","armando","bernays","trimmers","transom","grafts","columns","abelson","archway","infantries","orly","pock","selectors","lecterns","humps","kinked","bridles","essentials","instead","eliminating","mabel","zing","impersonation","cudgels","chang","artifacts","creon","clucking","skedaddled","spryer","footballs","honeys","wafer","knelt","flagstone","americanize","bohr","plottered","simone","conventional","definable","blackbirds","woodsier","carriage","residents","mezzanines","tenement","plymouth","wresting","islanders","malleable","attentively","irrelevancy","paulette","hillbillies","leech","cloaks","individualist","uncannier","patel","effusions","dungs","plugs","discompose","dacrons","teletypes","dismay","germany","travailing","loathes","devouter","chandelier","rinsed","denial","mil","outmanoeuvre","tugged","icings","reefer","dominicans","franz","destruct","bog","pinhole","jackknife","polytheists","chatted","tomfoolery","breeziness","beaked","tasman","possession","partying","shift","anodynes","pontificate","typefaces","mullions","reconnaissance","stanching","bedstead","belligerent","breakwaters","messerschmidt","instincts","sickle","quondam","limos","fosters","mentalities","minestrone","harrowed","folsom","travesty","compendiums","maladies","narrates","interlocks","humbleness","uplifted","slipknot","motorcyclists","restarted","iconoclast","forts","trumpery","cute","harpsichord","klutzier","ashtray","garlicking","sprayer","duodenal","parboiled","ultras","arkansan","metaphor","patterning","lorries","donetsk","coerced","constricted","murkiness","curtailing","bookish","tenacious","araucanian","unmask","forlorner","ills","bert","closures","cahoots","rotundity","sullying","pare","pretences","beggar","childproofs","educable","duct","posits","bushed","southward","echelon","approximates","spoonerism","waitresses","unman","isolation","suleiman","delight","skimping","rambles","redistrict","alderwomen","o","rejoiced","blot","backpedals","clearings","brontosauruses","laughingly","huckleberries","steinbeck","friskier","commander","skivvies","reality","intermingles","cumbersome","bribery","disagreeable","jersey","lamont","profiteered","shooters","transience","scraper","resignedly","grabbing","christies","piaget","executors","reproachfully","spasming","overproduction","incises","priesthoods","straightforwards","poesied","welled","bickered","drolleries","manures","daffy","segregate","waddles","cheerfully","overprinted","molester","lief","summarizes","vaccination","seminole","unlisted","rumping","ed","weir","manufacture","secretariat","fulminated","molybdenum","bakersfield","unpinning","heroism","violence","mistimed","alcoa","perter","manuscripts","separate","retractions","safes","atoll","grottos","boogieing","olga","frisking","grows","redeployment","helmholtz","durant","rankest","thespian","cheese","pilaf","thinness","contrast","parqueted","milkmaids","blackhead","breathlessly","bothering","decoration","arrogant","setups","contraptions","swirly","transgression","misses","handyman","snows","clinic","vatican","forecaster","haughtiness","bovine","strobe","ingram","maratha","descartes","billeting","treetop","aloud","globed","monument","argumentative","squeegee","especial","retrofits","artistes","propose","piraeus","horsetails","tailpipes","throughout","tarted","synods","unconcerned","weighting","duding","roe","undervalued","reachable","thicker","egging","dentistry","byte","distinguished","envisioning","filibusters","housewarming","matzot","dill","remarries","anatomical","kremlinologists","truancy","bostonians","limited","poorer","corniest","contradictory","three","temporaries","convivial","shirting","schisms","balconies","reinterpret","suturing","kumquats","oncology","unbidden","correlates","kowtows","flashest","neighborhood","rumbas","swathed","webb","birches","engages","promoters","outside","cheeriest","suffusion","propounding","bagels","amish","contrarily","xylophonists","familiarize","makes","testimony","crusaded","wildcatted","slackest","bovines","artier","plops","robbie","slosh","dinkier","airworthiest","carbohydrates","teammates","locoweed","stratagems","sarcoma","gougers","yuletide","rosemarie","upholster","sizzle","reminiscing","bluffers","shellac","heckled","hypothalami","showery","supposes","humbug","burnished","lopsided","imprisons","opine","leeches","generic","stimulated","soggily","aftershave","marvell","pekoe","microorganism","burlap","topples","misfire","scuttlebutt","tantrums","exits","eclecticism","alden","ilk","deltas","slack","effortlessly","operationally","offspring","staggers","alkalis","logger","spines","oscilloscope","tiniest","fluxed","collectively","leagues","procter","protruding","flukiest","underemployed","wetter","ignite","puddings","magnetosphere","solids","oceangoing","barrooms","refurnished","operational","mastering","white","organist","blackest","licentiates","marsupial","machinists","borderlands","dingies","kegging","dualism","cohen","existing","wheeler","uncleanly","umlauts","expiate","misspends","ebert","camber","adventured","weave","bounded","religiously","potluck","scions","millionths","goblet","witchery","dodge","sarasota","pier","membranous","stomaching","tallyhos","cohort","leveraged","makeshift","hexagon","thumped","zedong","versions","ultraconservatives","obeyed","pace","wicks","luncheoning","minerals","medications","moralizes","unites","rant","portents","apparelling","hums","farrowed","verve","boggiest","weal","josephus","perfects","beef","stairwell","comment","arrant","stature","kc","quoits","galls","adoption","reformulate","physicals","schroeder","scoundrels","delivered","crushed","rue","thrives","cerf","hijacker","inkier","vulvae","deterring","burgles","catechism","unhorse","reclined","dapple","angioplasties","sluggards","emceed","snobbery","accessory","cardiologist","browning","crosses","boasted","summonsing","gamble","overdue","scourge","dirges","cascades","precious","peacefuller","oysters","hoods","pirates","sauerkraut","whiskers","defames","repute","foolish","lactate","tharp","electrocutions","fating","freezers","invocation","dissenter","should","hells","homesickness","archdukes","preconceiving","scroungers","embellishment","massacre","upon","aerated","protuberant","sternly","meticulously","virulent","loch","enchant","raindrop","atrophies","magyar","interring","coachmen","exorcism","faintness","pointlessness","kawabata","installment","maliciously","vindicating","monkeying","uncanny","tangibles","blessed","forensic","arty","toppled","dilapidation","klutzes","moots","cottage","seismograph","diarists","aperitif","facing","filial","soundings","salsa","clear","cayenne","stilling","thighs","contrasting","cloistered","custodial","woodland","frillier","unrolls","landsat","chartres","toughly","saluted","verbose","transfiguring","zapped","iconoclasts","parkman","charlestons","spadework","okaying","numismatics","chestnuts","ghostwriters","nobelists","insouciant","vivisection","moods","edifices","relocated","wisdom","ignobly","namesakes","tapestry","schismatics","agra","blundering","sailboards","fruited","anticlimax","viewed","locus","barricading","rehearsed","irater","sibyl","steps","airsickness","blasphemous","swelling","salinger","veal","normalizes","gullet","inhabitant","slut","zinced","homing","headphone","chatters","winged","wingspread","kneecaps","tam","withdraws","repatriating","peter","isobars","dix","rekindled","snider","depends","mute","knowledgeably","mends","tides","stoutness","hempen","victoria","slaloming","buttons","grammars","astounding","memorandum","kenmore","solid","bandoliers","flowered","equivocation","assuredly","festers","helios","lebanese","impugned","shiftlessness","statement","announcer","vagueness","punctures","colonnade","exist","displeasing","diocletian","untold","unprintable","hereford","sidereal","joke","automatically","rendezvousing","surfed","surreptitious","depopulating","arching","massive","excise","beatles","rigorous","turnovers","impromptus","jezebels","glinted","leveraging","capsizing","voices","hitchhiking","ramon","wyeth","larva","unblushing","inanest","vacillate","contrives","kw","carboniferous","disinterred","predicated","song","andean","youths","previous","yours","supplicates","gompers","apprenticed","half","lactic","authenticating","charlatan","mendacious","flanks","hieronymus","dressy","owns","vestry","strobes","clapping","informers","sermoning","rifer","headstone","bobbing","forgiven","hypocritical","legation","adjusted","glibness","peeled","actuators","composition","payloads","abdication","delete","unnecessary","misprint","wooziest","cannibalistic","voiced","marooned","einstein","erratically","obsessions","impracticality","hoffa","rheumatics","handsets","tricked","afield","abdul","sounding","tray","massacring","iowan","grits","billy","purchases","profitably","resilience","eyed","vocabularies","golden","barking","riviera","helmsmen","cavorting","shrinks","hangmen","heliports","salve","assorting","neuroses","contribute","triathlon","adherents","gismo","sering","pulsate","hoarders","vacating","pulverization","destabilize","wore","eureka","gobs","raiding","valhalla","aureole","illustration","null","ageing","umbrellaing","characterize","ethel","bagging","lucas","nakedly","rinded","wainscottings","through","falter","clearness","smart","overspecializes","older","entourage","dawn"]
    print solution.anagrams(strs)
