https://mindsers.blog/post/https-using-nginx-certbot-docker/


# Install nginx on server

    sudo su

    yum install nginx
    
# Enable Env

source env/bin/activate

certbot --nginx -d dev1.dmtools.info

# Output

certbot --nginx -d dev1.dmtools.info
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Enter email address (used for urgent renewal and security notices)
 (Enter 'c' to cancel): andrew@gaitskell.com 

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.3-September-21-2022.pdf. You must
agree in order to register with the ACME server. Do you agree?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Would you be willing, once your first certificate is successfully issued, to
share your email address with the Electronic Frontier Foundation, a founding
partner of the Let's Encrypt project and the non-profit organization that
develops Certbot? We'd like to send you email about our work encrypting the web,
EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y
Account registered.
Requesting a certificate for dev1.dmtools.info

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/dev1.dmtools.info/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/dev1.dmtools.info/privkey.pem
This certificate expires on 2023-02-01.
These files will be updated when the certificate renews.

Deploying certificate
Successfully deployed certificate for dev1.dmtools.info to /etc/nginx/conf.d/dmtools.info.conf
Congratulations! You have successfully enabled HTTPS on https://dev1.dmtools.info

NEXT STEPS:
- The certificate will need to be renewed before it expires. Certbot can automatically renew the certificate in the background, but you may need to take steps to enable that functionality. See https://certbot.org/renewal-setup for instructions.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
If you like Certbot, please consider supporting our work by:
 * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
 * Donating to EFF:                    https://eff.org/donate-le
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(env) [root@fedora-vm-1 project]# 

