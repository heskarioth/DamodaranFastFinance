description = """
<img src="https://yt3.ggpht.com/ytc/AKedOLT08dzOY4vKFbEOpcb4wPvDzP_094qtI-1CTfxK=s900-c-k-c0x00ffffff-no-rj" alt="drawing" width="200"/>

## What's is this about?
DamodaranFastFinance is a onestop solution to help you find all the financial indicators you 
need to build your valuation, pricing, and corporate finance models, powered by FastAPI 🚀.

Very often the financial data needed to calculate beta, risk premiums and other indicators is often behind prohibitive paywalls or hard to obtain for those who can't afford to pay for a Bloomberg subscription.  
For those of us who didn't do a degree in finance but nonetheless have developed an itch for learning more about investing, educators like Professor Aswath Damodaran are the guiding light we need to nurture this interest of ours. I would like to thank professor Damodaran for the magnitude of information and courses he puts out online for free.
This is my little contribution to the cause.

**NB: Despite my gratitude I have to stress that this project has no affiliation whatsoever with Professor Aswath Damodaran. Again, it's simply a token of appreciation and support for the work made he made. All the data served by the endpoints is already present in the professor's website. I have simply created an open API for everyone keen on combining their learning from the courses with some development work.<br>No downloading of CSV files anymore, I've done that for you.**

<br><br><br><br><br>
To reach interactive mode follow the: /interactive endpoint.

## Future roadmaps
Some of the things I am expecting to work in the future include:
* **Documentation**. We all know Professor Damodaran doesn't exactly follow vanilla approaches to calculate financial indicators. For this reason I want to document and try to explain how each indicator is being calculated in a simple manner and have it next to the endpoint for quick reference explaination.
* **Performance**. The project followed synchronous programming, for this reason it might be quite slow once there is data from needs to be updated at the source level. In the next iteration I want to improve code performance by introducing concurrency.
* **Production deployment**. Due resource constraints / limited personal knowledge of production deployments, I have decided to use Heroku for deployment. I am quite aware its limitations. In the future, I'd like to try and deploy it in other platforms.
* **Monitoring**. Eventually I want to add monitoring feature to uderstand which endpoints users are more interest in. This will help me in multiple things such as rearranging endpoints orders, discouting unused ones, and overall improve the product.
* **Additional endpoints**. As of now, I have yet to include all endpoints provided by the professor. For instance, the whole section of pricing models data is missing. I am to include that and much more as I continue working on this project.


"""

tags_metadata = [
    {
        "name": "Essentials",
        "description": 
        """Most of the data is industry average per sector group. Before taking any data check which group your company belongs to.
        """
        
    },{
        "name": "Quick Enpoints",
        "description": 
        """Here you can quickly find the endpoints you'll probably need most if you were to do intrinsic valuation.
        """
        
    },
    {
        "name": "Cost of Equity",
        "description": "<br>Operations with users. The **login** logic is also here.",
    },
    {
        "name": "CashFlow Estimations",
        "description": "nada",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
    {
        "name": "Growth Rate Estimations",
        "description": "<br>Operations with users. The **login** logic is also here.",
    },
    {
        "name": "Capital Structure",
        "description": "<br>Operations with users. The **login** logic is also here.",
    },
    {
        "name": "Dividend Policy",
        "description": "<br>Operations with users. The **login** logic is also here.",
    },
    
]


contact={
        "name": "Camillo Heska",
        "url": "https://github.com/heskarioth",
        "email": "info@damodaranfastfinance.com",
    }

license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }


#![alt text](https://yt3.ggpht.com/ytc/AKedOLT08dzOY4vKFbEOpcb4wPvDzP_094qtI-1CTfxK=s900-c-k-c0x00ffffff-no-rj) 