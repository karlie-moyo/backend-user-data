# UoS Backend User Data

![image](https://github.com/user-attachments/assets/b077652a-dbaf-4919-931e-05126263b9c0)


Backend user authentication involves securely managing personal data, using basic and session authentication methods, and verifying identities with authentication services, often incorporating tokens like JWT and multi-factor authentication.
| PR.NO | PROJECT                                                                                                                                                 | DESCRIPTION |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| 0x00  | [Personal Data](./0x00-personal_data/)                                                                                      |Backend user data involves storing and managing personal information, such as names, emails, and passwords, securely in a backend system, ensuring privacy, data protection, and compliance with regulations like GDPR.|            
| 0x01  | [Basic Authentication](./0x01-Basic_authentication/)                                                                                     |**Basic authentication** is a simple authentication method where a user's credentials (username and password) are sent in an HTTP header, typically encoded in base64. It's easy to implement but not secure without additional measures like HTTPS.|
| 0x02  | [Session Authentication](./0x02-Session_authentication/)                                                                                      |**Session authentication** involves storing a user's authentication state on the server, typically in a session ID, which is stored in the user's browser as a cookie. The server validates the session ID for each request to maintain the user's authenticated state across multiple interactions.|                                                                                                                                                                 
| 0x03  | [User Authentication Service](./0x03-user_authentication_service/)                                                                  |A **user authentication service** verifies the identity of users by checking their credentials (e.g., username and password) against a database. It ensures secure access to applications by managing login, session, and token-based authentication (like JWT), often incorporating features like multi-factor authentication (MFA) for enhanced security.|

### AUTHOR:
<details>
    <summary>KARLIE MOYO</summary>
    <ul>
        <li>
            <a href="https://github.com/karlie-moyo">Github</a>
        </li>
        <li>
            <a href="https://twitter.com/karlieemoyo">Twitter</a>
        </li>
        <li>
            <a href="https://karlieemoyo@gmail.com">e-mail</a>
        </li>
    </ul>
</details>

---

### Acknowledgements  :pray:
___
All of the work in this project was conducted as part of the UoS-SE program's curriculum.
