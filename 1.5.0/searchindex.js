Search.setIndex({docnames:["getting_started","index","installation","kitchen_sink","modules","nyawc","nyawc.helpers","nyawc.http","nyawc.scrapers","options_callbacks","options_crawling_identity","options_crawling_scope","options_performance"],envversion:51,filenames:["getting_started.rst","index.rst","installation.rst","kitchen_sink.rst","modules.rst","nyawc.rst","nyawc.helpers.rst","nyawc.http.rst","nyawc.scrapers.rst","options_callbacks.rst","options_crawling_identity.rst","options_crawling_scope.rst","options_performance.rst"],objects:{"":{nyawc:[5,0,0,"-"]},"nyawc.Crawler":{Crawler:[5,1,1,""]},"nyawc.Crawler.Crawler":{_Crawler__crawler_finish:[5,2,1,""],_Crawler__crawler_start:[5,2,1,""],_Crawler__crawler_stop:[5,2,1,""],_Crawler__request_finish:[5,2,1,""],_Crawler__request_start:[5,2,1,""],_Crawler__spawn_new_request:[5,2,1,""],_Crawler__spawn_new_requests:[5,2,1,""],__init__:[5,2,1,""],__lock:[5,3,1,""],__options:[5,3,1,""],__stopped:[5,3,1,""],__stopping:[5,3,1,""],queue:[5,3,1,""],start_with:[5,2,1,""]},"nyawc.CrawlerActions":{CrawlerActions:[5,1,1,""]},"nyawc.CrawlerActions.CrawlerActions":{DO_AUTOFILL_FORM:[5,3,1,""],DO_CONTINUE_CRAWLING:[5,3,1,""],DO_NOT_AUTOFILL_FORM:[5,3,1,""],DO_SKIP_TO_NEXT:[5,3,1,""],DO_STOP_CRAWLING:[5,3,1,""]},"nyawc.CrawlerThread":{CrawlerThread:[5,1,1,""]},"nyawc.CrawlerThread.CrawlerThread":{__callback:[5,3,1,""],__callback_lock:[5,3,1,""],__init__:[5,2,1,""],__options:[5,3,1,""],__queue_item:[5,3,1,""],run:[5,2,1,""]},"nyawc.Options":{Options:[5,1,1,""],OptionsCallbacks:[5,1,1,""],OptionsIdentity:[5,1,1,""],OptionsPerformance:[5,1,1,""],OptionsScope:[5,1,1,""]},"nyawc.Options.Options":{__init__:[5,2,1,""],callbacks:[5,3,1,""],identity:[5,3,1,""],performance:[5,3,1,""],scope:[5,3,1,""]},"nyawc.Options.OptionsCallbacks":{_OptionsCallbacks__null_route_crawler_after_finish:[5,2,1,""],_OptionsCallbacks__null_route_crawler_before_start:[5,2,1,""],_OptionsCallbacks__null_route_form_after_autofill:[5,2,1,""],_OptionsCallbacks__null_route_form_before_autofill:[5,2,1,""],_OptionsCallbacks__null_route_request_after_finish:[5,2,1,""],_OptionsCallbacks__null_route_request_before_start:[5,2,1,""],__init__:[5,2,1,""],crawler_after_finish:[5,3,1,""],crawler_before_start:[5,3,1,""],form_after_autofill:[5,3,1,""],form_before_autofill:[5,3,1,""],request_after_finish:[5,3,1,""],request_before_start:[5,3,1,""]},"nyawc.Options.OptionsIdentity":{__init__:[5,2,1,""],cookies:[5,3,1,""],headers:[5,3,1,""]},"nyawc.Options.OptionsPerformance":{__init__:[5,2,1,""],max_threads:[5,3,1,""]},"nyawc.Options.OptionsScope":{__init__:[5,2,1,""],hostname_must_match:[5,3,1,""],max_depth:[5,3,1,""],protocol_must_match:[5,3,1,""],subdomain_must_match:[5,3,1,""],tld_must_match:[5,3,1,""]},"nyawc.Queue":{Queue:[5,1,1,""]},"nyawc.Queue.Queue":{_Queue__get_hash:[5,2,1,""],_Queue__get_var:[5,2,1,""],_Queue__set_var:[5,2,1,""],__init__:[5,2,1,""],__options:[5,3,1,""],add:[5,2,1,""],add_request:[5,2,1,""],count_cancelled:[5,3,1,""],count_errored:[5,3,1,""],count_finished:[5,3,1,""],count_in_progress:[5,3,1,""],count_queued:[5,3,1,""],count_total:[5,3,1,""],get_all:[5,2,1,""],get_first:[5,2,1,""],get_progress:[5,2,1,""],has_request:[5,2,1,""],move:[5,2,1,""]},"nyawc.QueueItem":{QueueItem:[5,1,1,""]},"nyawc.QueueItem.QueueItem":{STATUSES:[5,3,1,""],STATUS_CANCELLED:[5,3,1,""],STATUS_ERRORED:[5,3,1,""],STATUS_FINISHED:[5,3,1,""],STATUS_IN_PROGRESS:[5,3,1,""],STATUS_QUEUED:[5,3,1,""],__init__:[5,2,1,""],get_soup_response:[5,2,1,""],request:[5,3,1,""],response:[5,3,1,""],response_soup:[5,3,1,""],status:[5,3,1,""]},"nyawc.helpers":{HTTPRequestHelper:[6,0,0,"-"],RandomInputHelper:[6,0,0,"-"],URLHelper:[6,0,0,"-"]},"nyawc.helpers.HTTPRequestHelper":{HTTPRequestHelper:[6,1,1,""]},"nyawc.helpers.HTTPRequestHelper.HTTPRequestHelper":{complies_with_scope:[6,4,1,""],patch_with_options:[6,4,1,""]},"nyawc.helpers.RandomInputHelper":{RandomInputHelper:[6,1,1,""]},"nyawc.helpers.RandomInputHelper.RandomInputHelper":{cache:[6,3,1,""],get_for_type:[6,4,1,""],get_random_color:[6,4,1,""],get_random_email:[6,4,1,""],get_random_number:[6,4,1,""],get_random_password:[6,4,1,""],get_random_telephonenumber:[6,4,1,""],get_random_text:[6,4,1,""],get_random_url:[6,4,1,""],get_random_value:[6,4,1,""]},"nyawc.helpers.URLHelper":{URLHelper:[6,1,1,""]},"nyawc.helpers.URLHelper.URLHelper":{append_with_data:[6,4,1,""],cache:[6,3,1,""],get_hostname:[6,4,1,""],get_ordered_params:[6,4,1,""],get_path:[6,4,1,""],get_protocol:[6,4,1,""],get_subdomain:[6,4,1,""],get_tld:[6,4,1,""],is_mailto:[6,4,1,""],is_parsable:[6,4,1,""],make_absolute:[6,4,1,""]},"nyawc.http":{Handler:[7,0,0,"-"],Request:[7,0,0,"-"],Response:[7,0,0,"-"]},"nyawc.http.Handler":{Handler:[7,1,1,""]},"nyawc.http.Handler.Handler":{_Handler__content_type_matches:[7,2,1,""],_Handler__get_all_scrapers:[7,2,1,""],_Handler__get_all_scrapers_modules:[7,2,1,""],_Handler__make_request:[7,2,1,""],__init__:[7,2,1,""],__options:[7,3,1,""],__queue_item:[7,3,1,""],get_new_requests:[7,2,1,""]},"nyawc.http.Request":{Request:[7,1,1,""]},"nyawc.http.Request.Request":{METHOD_DELETE:[7,3,1,""],METHOD_GET:[7,3,1,""],METHOD_HEAD:[7,3,1,""],METHOD_OPTIONS:[7,3,1,""],METHOD_POST:[7,3,1,""],METHOD_PUT:[7,3,1,""],__init__:[7,2,1,""],cookies:[7,3,1,""],data:[7,3,1,""],depth:[7,3,1,""],headers:[7,3,1,""],method:[7,3,1,""],parent_raised_error:[7,3,1,""],url:[7,3,1,""]},"nyawc.http.Response":{Response:[7,1,1,""]},"nyawc.scrapers":{CSSRegexLinkScraper:[8,0,0,"-"],HTMLSoupFormScraper:[8,0,0,"-"],HTMLSoupLinkScraper:[8,0,0,"-"],JSONRegexLinkScraper:[8,0,0,"-"],XMLRegexLinkScraper:[8,0,0,"-"]},"nyawc.scrapers.CSSRegexLinkScraper":{CSSRegexLinkScraper:[8,1,1,""]},"nyawc.scrapers.CSSRegexLinkScraper.CSSRegexLinkScraper":{__init__:[8,2,1,""],__options:[8,3,1,""],__queue_item:[8,3,1,""],content_types:[8,3,1,""],get_requests:[8,2,1,""]},"nyawc.scrapers.HTMLSoupFormScraper":{HTMLSoupFormScraper:[8,1,1,""]},"nyawc.scrapers.HTMLSoupFormScraper.HTMLSoupFormScraper":{_HTMLSoupFormScraper__autofill_form_data:[8,2,1,""],_HTMLSoupFormScraper__get_default_form_data_input:[8,2,1,""],_HTMLSoupFormScraper__get_default_value_from_element:[8,2,1,""],_HTMLSoupFormScraper__get_form_data:[8,2,1,""],_HTMLSoupFormScraper__get_request:[8,2,1,""],_HTMLSoupFormScraper__get_valid_form_data_elements:[8,2,1,""],_HTMLSoupFormScraper__trim_grave_accent:[8,2,1,""],__init__:[8,2,1,""],__options:[8,3,1,""],__queue_item:[8,3,1,""],content_types:[8,3,1,""],get_requests:[8,2,1,""]},"nyawc.scrapers.HTMLSoupLinkScraper":{HTMLSoupLinkScraper:[8,1,1,""]},"nyawc.scrapers.HTMLSoupLinkScraper.HTMLSoupLinkScraper":{_HTMLSoupLinkScraper__trim_grave_accent:[8,2,1,""],__init__:[8,2,1,""],__options:[8,3,1,""],__queue_item:[8,3,1,""],content_types:[8,3,1,""],get_requests:[8,2,1,""]},"nyawc.scrapers.JSONRegexLinkScraper":{JSONRegexLinkScraper:[8,1,1,""]},"nyawc.scrapers.JSONRegexLinkScraper.JSONRegexLinkScraper":{__init__:[8,2,1,""],__options:[8,3,1,""],__queue_item:[8,3,1,""],content_types:[8,3,1,""],get_requests:[8,2,1,""]},"nyawc.scrapers.XMLRegexLinkScraper":{XMLRegexLinkScraper:[8,1,1,""]},"nyawc.scrapers.XMLRegexLinkScraper.XMLRegexLinkScraper":{__init__:[8,2,1,""],__options:[8,3,1,""],__queue_item:[8,3,1,""],content_types:[8,3,1,""],get_requests:[8,2,1,""]},nyawc:{Crawler:[5,0,0,"-"],CrawlerActions:[5,0,0,"-"],CrawlerThread:[5,0,0,"-"],Options:[5,0,0,"-"],Queue:[5,0,0,"-"],QueueItem:[5,0,0,"-"],helpers:[6,0,0,"-"],http:[7,0,0,"-"],scrapers:[8,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","attribute","Python attribute"],"4":["py","staticmethod","Python static method"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:attribute","4":"py:staticmethod"},terms:{"class":[5,6,7,8],"default":[0,3,5,8,9,10,11,12],"float":5,"function":3,"import":[0,3,9,10,11,12],"int":[3,5,6,7,9],"new":[0,1,3,5,6,7,8,10],"null":[0,3,5],"return":[0,3,5,6,7,8,9],"static":6,"true":[3,5,6,7,11],"var":5,And:11,For:[5,6,7,10],Not:1,The:[3,5,6,7,8,10,11,12],__callback:5,__callback_lock:5,__express:8,__get_hash:5,__init__:[5,7,8],__lock:5,__null_route_crawler_after_finish:5,__null_route_crawler_before_start:5,__null_route_form_after_autofil:5,__null_route_form_before_autofil:5,__null_route_request_after_finish:5,__null_route_request_before_start:5,__option:[5,7,8],__queue_item:[5,7,8],__stop:5,_crawler__crawler_finish:5,_crawler__crawler_start:5,_crawler__crawler_stop:5,_crawler__request_finish:5,_crawler__request_start:5,_crawler__spawn_new_request:5,_handler__content_type_match:7,_handler__get_all_scrap:7,_handler__get_all_scrapers_modul:7,_handler__make_request:7,_htmlsoupformscraper__autofill_form_data:8,_htmlsoupformscraper__get_default_form_data_input:8,_htmlsoupformscraper__get_default_value_from_el:8,_htmlsoupformscraper__get_form_data:8,_htmlsoupformscraper__get_request:8,_htmlsoupformscraper__get_valid_form_data_el:8,_htmlsoupformscraper__trim_grave_acc:8,_htmlsouplinkscraper__trim_grave_acc:8,_optionscallbacks__null_route_crawler_after_finish:5,_optionscallbacks__null_route_crawler_before_start:5,_optionscallbacks__null_route_form_after_autofil:5,_optionscallbacks__null_route_form_before_autofil:5,_optionscallbacks__null_route_request_after_finish:5,_optionscallbacks__null_route_request_before_start:5,_queue__get_hash:5,_queue__get_var:5,_queue__set_var:5,abcdefghijklmnopqrstuvwxyz:6,about:5,absolut:[6,7,8],accent:8,action:5,actual:5,add:[1,5],add_request:5,address:6,after:[0,3,5],again:1,agent:[3,6,10],all:[1,2,3,5,7,8,9,10,11],almost:3,alreadi:5,also:[3,6,9,11],amount:[3,5,9,12],ani:9,anoth:5,anyth:3,api:7,append:6,append_with_data:6,applewebkit:[3,10],applic:[1,5,8],argument:9,arr:5,arrai:9,attribut:8,autofil:[3,5,8],automat:9,avail:[2,5,7],available_content_typ:7,averag:[1,2],base:[5,6,7,8],beautifulsoup4:9,beautifulsoup:[5,8],becaus:[5,6,8],befor:[0,3,5,7],being:5,below:[3,10],blech:[3,10],bodi:9,bool:[5,6,7],both:6,build:8,built:5,cach:[5,6],calcul:5,call:[0,3,5,7,9],callback:[0,3,5],callback_lock:5,callbacks_exampl:9,can:[3,5,7,8,9,10],cancel:5,caract:6,cascad:8,caus:5,cb_crawler_after_finish:[0,3,9],cb_crawler_before_start:[0,3,9],cb_form_after_autofil:[3,9],cb_form_before_autofil:[3,9],cb_request_after_finish:[0,3,9],cb_request_before_start:[0,3,9],certain:5,chanc:11,charact:6,character_set:6,check:[5,6,7,10],chrome:[3,10],client:8,code:[5,9],collis:5,color:6,com:[0,2,3,5,6,9,10,11,12],complex:5,compli:6,complies_with_scop:6,condit:5,construct:[5,7,8],contain:[3,5,6,7,8,9],content:[7,8],content_typ:[7,8],continu:[5,9],cooki:[3,5,7,10],could:5,count:5,count_cancel:5,count_error:5,count_finish:[3,5],count_in_progress:5,count_queu:5,count_tot:[3,5],crawl:[0,1,3,5,6,7,9,12],crawler:[1,2,3,4,10,11,12],crawler_after_finish:[0,3,5,9],crawler_before_start:[0,3,5,9],crawleract:[0,3,4,9],crawlerthread:4,creat:5,css:8,cssregexlinkscrap:[4,5],current:[5,7,8,9],custom:10,data:[1,3,6,7,8,9],declar:3,deeper:[3,11],def:[0,3,9],defin:5,delet:7,depth:[3,5,7,11],detail:7,dict:[5,7,8],did:5,differ:[5,6],digit:6,discov:2,do_autofill_form:[3,5,9],do_continue_crawl:[0,3,5,9],do_not_autofill_form:[3,5,9],do_skip_to_next:[3,5,9],do_stop_crawl:[3,5,9],doc:[5,7],doe:9,doesn:8,domain:[1,3,10],duplic:[1,5],dure:[5,9],easy_instal:2,edit:9,either:5,element:[3,5,8,9],elsewher:[3,10],email:6,empti:[1,5,8],enabl:[1,5],english:3,entir:9,entri:5,error:[5,7],everi:[1,5],everyth:[3,5],exampl:[0,3,5,6,10],except:[1,5],execut:[5,7,8,9],exist:[5,6],express:8,extract:2,fals:[3,5,6,7,11],field:5,file:2,fill:9,find:[7,8],finish:[0,1,3,5,7],finnwea:[0,3,5,9,10,11,12],first:[1,5],footprint:5,form:[3,5,6,8],form_after_autofil:[3,5,9],form_before_autofil:[3,5,9],form_data:[3,5,8,9],format:[0,6,9],found:[0,1,3,5,6,7,8,9,11],from:[0,3,5,6,8,9,10,11,12],ftp:6,gecko:[3,10],gener:[5,6],get:[1,5,6,7,8],get_al:[3,5,9],get_count:[0,9],get_first:5,get_for_typ:6,get_hostnam:6,get_new_request:7,get_ordered_param:6,get_path:6,get_progress:[3,5,9],get_protocol:6,get_random_color:6,get_random_email:6,get_random_numb:6,get_random_password:6,get_random_telephonenumb:6,get_random_text:6,get_random_url:6,get_random_valu:6,get_request:8,get_soup_respons:5,get_subdomain:6,get_tld:6,github:2,given:[5,6,7,8],goe:[1,3],grave:8,gross_cooki:[3,10],handl:5,handler:[4,5],has:[5,8],has_request:5,hash:[5,6],have:[2,5],head:7,header:[3,5,7,10],helper:[4,5],hex:6,higher:2,host:8,hostnam:[3,5,6,11],hostname_must_match:[3,5,11],href:8,html:[6,8],htmlsoupformscrap:[4,5],htmlsouplinkscrap:[4,5],http:[0,2,3,4,5,6,8,9,10,11,12],httprequesthelp:[4,5],ident:[3,5],identity_exampl:10,imag:8,improv:5,in_progress:5,includ:[5,6],index:5,infinit:[5,6],inform:[5,7],initi:5,input:[6,8,9],input_typ:6,instanc:[5,7,8],instead:[1,5],is_mailto:6,is_pars:6,item:[5,6,7,8,9],items_cancel:5,items_error:5,items_finish:5,items_in_progress:5,items_queu:5,iter:[5,9],jar:[5,7,10],json:8,jsonregexlinkscrap:[4,5],keep:[1,5],kei:[5,6,7,8,10],khtml:[3,10],left:5,length:6,level:[3,11],like:[3,9,10],line:5,link:2,list:[5,6,7,8],lock:5,log:0,loop:6,ltd:6,mailto:6,main:[1,5],make:[2,3,5,6,7,9,10],make_absolut:6,manag:5,manual:8,mark:5,master:[5,7],match:[7,11],max:[1,5],max_depth:[3,5,11],max_thread:[3,5,12],maximum:[3,5,11,12],mean:3,method:[3,5,7,9],method_delet:7,method_get:7,method_head:7,method_opt:7,method_post:7,method_put:7,modul:4,moment:5,more:[5,7],most:6,move:5,mozilla:[3,10],multipl:5,must:[6,11],name:[3,5,8,10],need:[5,6],never:11,new_queue_item:[0,3,5,9],new_queue_item_statu:5,new_request:[5,6],next:5,none:[3,5,6,7,11],normal:9,note:[1,9,11],now:9,number:6,nyawc:[0,2,3,9,10,11,12],obj:[5,6,7,8],object:[5,6,7,8,10],one:[3,5,7,9,11],ongo:5,onli:[3,5,6,9,11],option:[0,1,3,4,6,7,8,9],optionscallback:5,optionsident:5,optionsperform:5,optionsscop:[5,6],ordereddict:[6,7],org:[5,7],otherwis:[5,6,7],output:0,over:[5,9],packag:4,page:[3,5,6,11],pair:[5,6,9],paramet:[5,6,7,8],parent:[5,6,7,8],parent_queue_item:6,parent_raised_error:7,pars:6,parsabl:6,pass:[3,9],password:6,patch:6,patch_with_opt:6,path:[3,6,10],percentag:[3,5,9],perfectli:5,perform:[3,5],performance_exampl:12,phone:6,phrase:3,piec:5,placehold:7,pleas:[1,9,10,11],possibl:6,post:[1,7,9],postdata:3,prevent:[5,6],print:[0,3,9],process:5,progress:5,project:2,protocol:[3,5,6,11],protocol_must_match:[3,5,11],purpos:[1,6],put:7,pypi:2,python:[0,1,2,5,7,10],queri:6,queu:5,queue:[0,1,3,4,6,7,8,9],queue_item:[0,3,5,6,7,8,9],queueitem:[3,4,6,7,8,9],quickstart:5,quit:5,race:5,rais:[5,7],random:[5,6,8,9],randominputhelp:[4,5],reach:[1,5],realli:6,receiv:9,recurs:5,refer:7,regular:8,rel:[6,8],releas:2,repeat:1,replac:7,request:[0,1,3,4,5,6,8,10,11,12],request_after_finish:[0,3,5,9],request_before_start:[0,3,5,9],requir:[5,6],respons:[1,3,4,5,6,8,9],response_soup:5,retriev:7,rout:[0,3,5],run:[2,5,9],runtim:5,safari:[3,10],same:[3,5,6,11],scan:1,scanner:1,scope:[3,5,6],scope_exampl:11,scrape:[5,8],scraper:[4,5,7],search:[3,5,6,11],see:5,sent:7,session:5,set:[3,5,6,10,11],settin:[5,7,8],setup:2,sheet:8,should:[5,6],shown:10,side:8,sigint:5,simultan:[3,5,12],sinc:5,skip:[5,9],sleep:5,some:9,soup:[5,8],sourc:[5,6,7,8],spawn:[1,5],specifi:[1,7],src:6,stackoverflow:5,start:[1,3,5,11],start_with:[0,3,5,9,10,11,12],startpoint:[3,5,11],statu:5,status:5,status_cancel:5,status_cod:[3,9],status_error:5,status_finish:[3,5],status_in_progress:5,status_queu:5,step:1,stop:[1,5,9,11],str:[0,3,5,6,7,8,9],string:6,strong:6,style:8,subdomain:[3,5,6,11],subdomain_must_match:[3,5,11],submodul:4,subpackag:4,support:8,sure:[2,6],svg:8,tasty_cooki:[3,10],telephon:6,test:[2,6],text:[5,6,8,9],thi:[5,6,7,9,11],think:3,thread:[1,3,5,12],three:9,tijm:2,time:[5,6],tld:[3,5,6,11],tld_must_match:[3,5,11],top:5,total:5,total_request:[3,9],track:[1,5],treat:6,trim:8,two:[6,9],type:[5,6,7,8],unit:2,unittest:2,unlimit:[3,5,11],until:[1,5],updat:8,upgrad:2,url:[0,1,3,6,7,8,9],urlhelp:[4,5],use:[3,5,6,7],used:[1,5,6,7,9],useful:1,user:[3,5,6,10],uses:5,using:[5,8,10],valid:[6,8],valu:[3,5,6,7,8,9,10],variabl:5,veri:1,verifi:2,version:2,vulner:1,web:[1,2],were:[5,7,8,9],when:[5,7,8,9],where:5,which:[5,9],win64:[3,10],window:[3,10],without:[5,8],work:[2,5],would:[5,6],x64:[3,10],xhtml:8,xml:8,xmlregexlinkscrap:[4,5],yet:5,you:[1,2,10,11],your:[1,2],yum:[3,10]},titles:["Getting started","Welcome to the N.Y.A.W.C documentation","Installation","Kitchen sink","nyawc","nyawc package","nyawc.helpers package","nyawc.http package","nyawc.scrapers package","Callbacks","Crawling identity","Crawling scope","Performance"],titleterms:{after:9,autofil:9,avail:[9,10,11,12],background:0,befor:9,callback:9,clone:2,content:[0,2,9,10,11,12],crawl:[10,11],crawler:[0,5,9],crawleract:5,crawlerthread:5,cssregexlinkscrap:8,document:1,download:2,easyinstal:2,finish:9,foreground:0,form:9,get:0,git:2,handler:7,helper:6,how:[1,9,10,11,12],htmlsoupformscrap:8,htmlsouplinkscrap:8,http:7,httprequesthelp:6,ident:10,implement:0,instal:2,jsonregexlinkscrap:8,kitchen:3,minim:0,modul:[5,6,7,8],nyawc:[4,5,6,7,8],option:[5,10,11,12],packag:[5,6,7,8],perform:12,pip:2,queue:5,queueitem:5,randominputhelp:6,request:[7,9],respons:7,run:0,scope:11,scraper:8,sink:3,start:[0,9],submodul:[5,6,7,8],subpackag:5,tabl:[0,2,9,10,11,12],urlhelp:6,use:[9,10,11,12],using:2,welcom:1,work:1,xmlregexlinkscrap:8,zip:2}})