# Exercise 2.1 Getting Started with Django Questions

## Why is Django so popular among web developers?

Django is a highly popular Python framework for web development due to its "batteries-included" approach, offering essential features like user-friendly admin panels, authentication, and content delivery support. Its Model View Template (MVT) architecture ensures fast, scalable, and loosely coupled application development, suitable for projects of any size. Django emphasizes efficient and maintainable code through DRY principles, provides robust security with built-in encryption, and is backed by a strong open-source community for support and scalability. Additionally, it integrates seamlessly with CDNs and content management systems, making it ideal for handling large-scale content and data.

## List 5 companies that use Django. Specify what the company’s product or service is and what they use Django for.

**Instagram**, a global photo and video sharing social media platform, uses Django’s ability to handle rapid development and scalability. Django’s ORM manages Instagram’s huge databases efficiently. It powers it’s web-based interfaces and API endpoints, ensuring a seamless experience for millions of users.

**Pinterest**, a visual content-sharing platform and social network, used Django’s rapid prototyping features to handle it’s web interfaces, manage content and support API integrations.

**Youtube**, a video-sharing platform and live TV streaming service, uses Django to manage the backend for subscription services and user interaction. Django help streamline authentication, payment processing content delivery for users.

**Spotify**, a music streaming service, uses Django to support Spotify’s recommendation algorithms, this allows effective handling of user data, playlists and real-time updates.

**Dropbox**, a cloud storage and file sharing service, uses Django for handling authentication and API integrations. 

## Explain if you would use Django for the following scenarios:

***You need to develop a web application with multiple users***  
Django would be ideal to build this app. Scalability is one of Django’s key benefit, and can handle a large number of users and requests efficiently, and has a built-in authentication and authorisation system.  

***You need fast deployment and the ability to make changes as you proceed***  
Django is well suited for this scenario. As it’s based on MVT it is ideal where fast prototyping, a lot of changes and high-speed applications are required.

***You need to build a very basic application, which doesn’t require any database access or file operations***  
Django wouldn’t be a suitable framework to use in this scenario as database access isn’t required. Django would only be suitable if an application needs both a backend (database) and frontend. As it has a lot of prewritten code it is server intensive which makes it heavy on low-bandwidth systems, this is best avoided if not required. 

***You want to build an application from scratch and want a lot of control over how it works***  
Django would be unsuitable here. As Django is a batteries-included system and works the specific Django way, it is less suitable for applications where you need a lot of control over the internals of the system. Developers must follow the “Django Way”

***You’re about to start working on a big project and are afraid of getting stuck and needing additional support.***   
Django would be ideal to use here as it is open source and has a large community, which offers lots of support. 