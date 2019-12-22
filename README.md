
# Option 4

- agi set debug on
- chmod 777 
- install pyst2 w/ pip

# Git    :wavy_dash:

 [Tutorial](https://github.com/bmalbusca/git_getting_started) (click here!)



________

# RSI_VOIP ()

 *Project files - Asterisk* 

  - sip.conf (users)
  - extension.conf (rules)


## 1. Use a VM with Asterisk as Server (Virtual Box and MAC)

1. Install Virtual Box
2. Install extensions pack for Virtual Box (enable en0 and IP forwarding)
3. Add Network option at VM "System" tab.
4. Add NAT to Adapter 1
5. Go to Tools and add/create an adapter interface
6. Return to "Network" tab. Add Host-only Adapter to Adapter 2  using the adapter interface   



## 2. How to setup your X-Lite on MAC (softphone)

1. Go to your VM and run ``terminal@:~ ip a``
2. Add the IP to Domain form
3. Add the User ID and secret to sip.conf. Check the update with the following commands (after running the server)  
``terminal@:asterisk~ ip a sip reload`` and ``terminal@:asterisk~ sip show peers``
4. Fill the ID and secret into User ID and Password respectively
5. Choose Domain Proxy and Domain outbound. 
6. Run the Server (VM) using the command ``terminal@:~ sudo asterisk -vvvvr``
7. Run the X-lite 

***Done***


#POST Request - CTT POSTAL

``` curl -X POST -H 'Content-Type: application/json'  http://www.ctt.pt/feapl_2/app/open/postalCodeSearch/postalCodeSearch.jspx\?cp4\=1000\&cp3\=048\&method%3AsearchPC2\=Procurar ```
