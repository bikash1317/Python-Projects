import re
str1 = ''' 

Page semi-protected
Email
From Wikipedia, the free encyclopedia
Jump to navigationJump to search
For the company, see Email Limited. "Inbox" redirects here; for the Google product, see Inbox by Gmail.

This screenshot shows the "Inbox" page of an email client; users can see new emails and take actions, such as reading, deleting, saving, or responding to these messages.

The at sign, a part of every SMTP email address[1]
Electronic mail (email or e-mail) is a method of exchanging messages ("mail") between people using electronic devices. Email entered limited use in the 1960s, but users could only send to users of the same computer, and some early email systems required the author and the recipient to both be online simultaneously, similar to instant messaging. Ray Tomlinson is credited as the inventor of email; in 1971, he developed the first system able to send mail between users on different hosts across the ARPANET, using the @ sign to link the user name with a destination server. By the mid-1970s, this was the form recognized as email.

Email operates across computer networks, primarily the Internet. Today's email systems are based on a store-and-forward model. Email servers accept, forward, deliver, and store messages. Neither the users nor their computers are required to be online simultaneously; they need to connect, typically to a mail server or a webmail interface to send or receive messages or download it.

Originally an ASCII text-only communications medium, Internet email was extended by Multipurpose Internet Mail Extensions (MIME) to carry text in other character sets and multimedia content attachments. International email, with internationalized email addresses using UTF-8, is standardized but not widely adopted.[2]

The history of modern Internet email services reaches back to the early ARPANET, with standards for encoding email messages published as early as 1973 (RFC 561). An email message sent in the early 1970s is similar to a basic email sent today.


Contents
1	Terminology
2	Origin
3	Operation
4	Message format
4.1	Message header
4.1.1	Header fields
4.2	Message body
4.2.1	Content encoding
4.2.2	Plain text and HTML
5	Servers and client applications
5.1	Filename extensions
5.2	URI scheme mailto
6	Types
6.1	Web-based email
6.2	POP3 email servers
6.3	IMAP email servers
6.4	MAPI email servers
7	Uses
7.1	Business and organizational use
7.1.1	Email marketing
7.2	Personal use
7.2.1	Personal computer
7.2.2	Mobile
7.2.3	Declining use among young people
8	Issues
8.1	Attachment size limitation
8.2	Information overload
8.3	Spam
8.4	Malware
8.5	Email spoofing
8.6	Email bombing
8.7	Privacy concerns
8.8	Legal contracts
8.9	Flaming
8.10	Email bankruptcy
8.11	Internationalization
8.12	Tracking of sent mail
9	See also
10	Notes
11	References
12	Further reading
13	External links
Terminology
Historically, the term electronic mail is any electronic document transmission. For example, several writers in the early 1970s used the term to refer to fax document transmission.[3][4] As a result, finding its first use is difficult with the specific meaning it has today.

The term electronic mail has been in use with its current meaning since at least 1975, and variations of the shorter E-mail have been in use since at least 1979:[5][6]

email is now the common form, and recommended by style guides.[7][8] It is the form required by IETF Requests for Comments (RFC) and working groups.[9] This spelling also appears in most dictionaries.[10][11][12][13][14][15][16]
e-mail is the form favored in edited published American English and British English writing as reflected in the Corpus of Contemporary American English data,[17] but is falling out of favor in some style guides.[8][18]
EMail is a traditional form used in RFCs for the "Author's Address" and is required "for historical reasons".[19]
E-mail is sometimes used, capitalizing the initial E as in similar abbreviations like E-piano, E-guitar, A-bomb, and H-bomb.[20]
In the original protocol, RFC 524, none of these forms was used. The service is simply referred to as mail, and a single piece of electronic mail is called a message.

An Internet e-mail consists of an envelope and content;[21] the content consists of a header and a body.[22]

Origin
Main article: History of email
Computer-based mail and messaging became possible with the advent of time-sharing computers in the early 1960s, and informal methods of using shared files to pass messages were soon expanded into the first mail systems. Most developers of early mainframes and minicomputers developed similar, but generally incompatible, mail applications. Over time, a complex web of gateways and routing systems linked many of them. Many US universities were part of the ARPANET (created in the late 1960s), which aimed at software portability between its systems. In 1971 the first ARPANET network email was sent, introducing the now-familiar address syntax with the '@' symbol designating the user's system address.[23] The Simple Mail Transfer Protocol (SMTP) protocol was introduced in 1981.

For a time in the late 1980s and early 1990s, it seemed likely that either a proprietary commercial system or the X.400 email system, part of the Government Open Systems Interconnection Profile (GOSIP), would predominate.[nb 1] However, once the final restrictions on carrying commercial traffic over the Internet ended in 1995,[24][25] a combination of factors made the current Internet suite of SMTP, POP3 and IMAP email protocols the standard.

Operation
The following is a typical sequence of events that takes place when sender Alice transmits a message using a mail user agent (MUA) addressed to the email address of the recipient.[26]


Email operation
The MUA formats the message in email format and uses the submission protocol, a profile of the Simple Mail Transfer Protocol (SMTP), to send the message content to the local mail submission agent (MSA), in this case smtp.a.org.
The MSA determines the destination address provided in the SMTP protocol (not from the message header) — in this case, bob@b.org — which is a fully qualified domain address (FQDA). The part before the @ sign is the local part of the address, often the username of the recipient, and the part after the @ sign is a domain name. The MSA resolves a domain name to determine the fully qualified domain name of the mail server in the Domain Name System (DNS).
The DNS server for the domain b.org (ns.b.org) responds with any MX records listing the mail exchange servers for that domain, in this case mx.b.org, a message transfer agent (MTA) server run by the recipient's ISP.[27]
smtp.a.org sends the message to mx.b.org using SMTP. This server may need to forward the message to other MTAs before the message reaches the final message delivery agent (MDA).
The MDA delivers it to the mailbox of user bob.
Bob's MUA picks up the message using either the Post Office Protocol (POP3) or the Internet Message Access Protocol (IMAP).
In addition to this example, alternatives and complications exist in the email system:

Alice or Bob may use a client connected to a corporate email system, such as IBM Lotus Notes or Microsoft Exchange. These systems often have their own internal email format and their clients typically communicate with the email server using a vendor-specific, proprietary protocol. The server sends or receives email via the Internet through the product's Internet mail gateway which also does any necessary reformatting. If Alice and Bob work for the same company, the entire transaction may happen completely within a single corporate email system.
Alice may not have an MUA on her computer but instead may connect to a webmail service.
Alice's computer may run its own MTA, so avoiding the transfer at step 1.
Bob may pick up his email in many ways, for example logging into mx.b.org and reading it directly, or by using a webmail service.
Domains usually have several mail exchange servers so that they can continue to accept mail even if the primary is not available.
Many MTAs used to accept messages for any recipient on the Internet and do their best to deliver them. Such MTAs are called open mail relays. This was very important in the early days of the Internet when network connections were unreliable.[28][29] However, this mechanism proved to be exploitable by originators of unsolicited bulk email and as a consequence open mail relays have become rare,[30] and many MTAs do not accept messages from open mail relays.

Message format
The basic Internet message format used for email[31] is defined by RFC 5322, with encoding of non-ASCII data and multimedia content attachments defined in RFC 2045 through RFC 2049, collectively called Multipurpose Internet Mail Extensions or MIME. The extensions in International email apply only to email. RFC 5322 replaced the earlier RFC 2822 in 2008, then RFC 2822 in 2001 replaced RFC 822 – the standard for Internet email for decades. Published in 1982, RFC 822 was based on the earlier RFC 733 for the ARPANET.[32]

Internet email messages consist of two sections, 'header' and 'body'. These are known as 'content'.[33][34] The header is structured into fields such as From, To, CC, Subject, Date, and other information about the email. In the process of transporting email messages between systems, SMTP communicates delivery parameters and information using message header fields. The body contains the message, as unstructured text, sometimes containing a signature block at the end. The header is separated from the body by a blank line.

Message header
RFC 5322 specifies the syntax of the email header. Each email message has a header (the "header section" of the message, according to the specification), comprising a number of fields ("header fields"). Each field has a name ("field name" or "header field name"), followed by the separator character ":", and a value ("field body" or "header field body").

Each field name begins in the first character of a new line in the header section, and begins with a non-whitespace printable character. It ends with the separator character ":". The separator follows the field value (the "field body"). The value can continue onto subsequent lines if those lines have space or tab as their first character. Field names and, without SMTPUTF8, field bodies are restricted to 7-bit ASCII characters. Some non-ASCII values may be represented using MIME encoded words.

Header fields
Email header fields can be multi-line, with each line recommended to be no more than 78 characters, although the limit is 998 characters.[35] Header fields defined by RFC 5322 contain only US-ASCII characters; for encoding characters in other sets, a syntax specified in RFC 2047 may be used.[36] In some examples, the IETF EAI working group defines some standards track extensions,[37][38] replacing previous experimental extensions so UTF-8 encoded Unicode characters may be used within the header. In particular, this allows email addresses to use non-ASCII characters. Such addresses are supported by Google and Microsoft products, and promoted by some government agents.[39]

The message header must include at least the following fields:[40][41]

From: The email address, and, optionally, the name of the author(s). Some email clients are changeable through account settings.
Date: The local time and date the message was written. Like the From: field, many email clients fill this in automatically before sending. The recipient's client may display the time in the format and time zone local to them.
RFC 3864 describes registration procedures for message header fields at the IANA; it provides for permanent and provisional field names, including also fields defined for MIME, netnews, and HTTP, and referencing relevant RFCs. Common header fields for email include:[42]

To: The email address(es), and optionally name(s) of the message's recipient(s). Indicates primary recipients (multiple allowed), for secondary recipients see Cc: and Bcc: below.
Subject: A brief summary of the topic of the message. Certain abbreviations are commonly used in the subject, including "RE:" and "FW:".
Cc: Carbon copy; Many email clients mark email in one's inbox differently depending on whether they are in the To: or Cc: list.
Bcc: Blind carbon copy; addresses are usually only specified during SMTP delivery, and not usually listed in the message header.
Content-Type: Information about how the message is to be displayed, usually a MIME type.
Precedence: commonly with values "bulk", "junk", or "list"; used to indicate automated "vacation" or "out of office" responses should not be returned for this mail, e.g. to prevent vacation notices from sent to all other subscribers of a mailing list. Sendmail uses this field to affect prioritization of queued email, with "Precedence: special-delivery" messages delivered sooner. With modern high-bandwidth networks, delivery priority is less of an issue than it was. Microsoft Exchange respects a fine-grained automatic response suppression mechanism, the X-Auto-Response-Suppress field.[43]
Message-ID: Also an automatic-generated field to prevent multiple deliveries and for reference in In-Reply-To: (see below).
In-Reply-To: Message-ID of the message this is a reply to. Used to link related messages together. This field only applies to reply messages.
References: Message-ID of the message this is a reply to, and the message-id of the message the previous reply was a reply to, etc.
Reply-To: Address should be used to reply to the message.
Sender: Address of the sender acting on behalf of the author listed in the From: field (secretary, list manager, etc.).
Archived-At: A direct link to the archived form of an individual email message.
The To: field may be unrelated to the addresses to which the message is delivered. The delivery list is supplied separately to the transport protocol, SMTP, which may be extracted from the header content. The "To:" field is similar to the addressing at the top of a conventional letter delivered according to the address on the outer envelope. In the same way, the "From:" field may not be the sender. Some mail servers apply email authentication systems to messages relayed. Data pertaining to the server's activity is also part of the header, as defined below.

SMTP defines the trace information of a message saved in the header using the following two fields:[44]

Received: after an SMTP server accepts a message, it inserts this trace record at the top of the header (last to first).
Return-Path: after the delivery SMTP server makes the final delivery of a message, it inserts this field at the top of the header.
Other fields added on top of the header by the receiving server may be called trace fields.[45]

Authentication-Results: after a server verifies authentication, it can save the results in this field for consumption by downstream agents.[46]
Received-SPF: stores results of SPF checks in more detail than Authentication-Results.[47]
DKIM-Signature: stores results of DomainKeys Identified Mail (DKIM) decryption to verify the message was not changed after it was sent.[48]
Auto-Submitted: is used to mark automatic-generated messages.[49]
VBR-Info: claims VBR whitelisting[50]
Message body
Content encoding
Internet email was designed for 7-bit ASCII.[51] Most email software is 8-bit clean, but must assume it will communicate with 7-bit servers and mail readers. The MIME standard introduced character set specifiers and two content transfer encodings to enable transmission of non-ASCII data: quoted printable for mostly 7-bit content with a few characters outside that range and base64 for arbitrary binary data. The 8BITMIME and BINARY extensions were introduced to allow transmission of mail without the need for these encodings, but many mail transport agents may not support them. In some countries, several encoding schemes co-exist; as the result, by default, the message in a non-Latin alphabet language appears in non-readable form (the only exception is a coincidence if the sender and receiver use the same encoding scheme). Therefore, for international character sets, Unicode is growing in popularity.[citation needed]

Plain text and HTML
Most modern graphic email clients allow the use of either plain text or HTML for the message body at the option of the user. HTML email messages often include an automatic-generated plain text copy for compatibility. Advantages of HTML include the ability to include in-line links and images, set apart previous messages in block quotes, wrap naturally on any display, use emphasis such as underlines and italics, and change font styles. Disadvantages include the increased size of the email, privacy concerns about web bugs, abuse of HTML email as a vector for phishing attacks and the spread of malicious software.[52]

Some web-based mailing lists recommend all posts be made in plain-text, with 72 or 80 characters per line for all the above reasons,[53][54] and because they have a significant number of readers using text-based email clients such as Mutt. Some Microsoft email clients may allow rich formatting using their proprietary Rich Text Format (RTF), but this should be avoided unless the recipient is guaranteed to have a compatible email client.[55]

Servers and client applications

The interface of an email client, Thunderbird.
Messages are exchanged between hosts using the Simple Mail Transfer Protocol with software programs called mail transfer agents (MTAs); and delivered to a mail store by programs called mail delivery agents (MDAs, also sometimes called local delivery agents, LDAs). Accepting a message obliges an MTA to deliver it,[56] and when a message cannot be delivered, that MTA must send a bounce message back to the sender, indicating the problem.

Users can retrieve their messages from servers using standard protocols such as POP or IMAP, or, as is more likely in a large corporate environment, with a proprietary protocol specific to Novell Groupwise, Lotus Notes or Microsoft Exchange Servers. Programs used by users for retrieving, reading, and managing email are called mail user agents (MUAs).

Mail can be stored on the client, on the server side, or in both places. Standard formats for mailboxes include Maildir and mbox. Several prominent email clients use their own proprietary format and require conversion software to transfer email between them. Server-side storage is often in a proprietary format but since access is through a standard protocol such as IMAP, moving email from one server to another can be done with any MUA supporting the protocol.

Many current email users do not run MTA, MDA or MUA programs themselves, but use a web-based email platform, such as Gmail or Yahoo! Mail, that performs the same tasks.[57] Such webmail interfaces allow users to access their mail with any standard web browser, from any computer, rather than relying on a local email client.

Filename extensions
Upon reception of email messages, email client applications save messages in operating system files in the file system. Some clients save individual messages as separate files, while others use various database formats, often proprietary, for collective storage. A historical standard of storage is the mbox format. The specific format used is often indicated by special filename extensions:

eml
Used by many email clients including Novell GroupWise, Microsoft Outlook Express, Lotus notes, Windows Mail, Mozilla Thunderbird, and Postbox. The files contain the email contents as plain text in MIME format, containing the email header and body, including attachments in one or more of several formats.
emlx
Used by Apple Mail.
msg
Used by Microsoft Office Outlook and OfficeLogic Groupware.
mbx
Used by Opera Mail, KMail, and Apple Mail based on the mbox format.
Some applications (like Apple Mail) leave attachments encoded in messages for searching while also saving separate copies of the attachments. Others separate attachments from messages and save them in a specific directory.

URI scheme mailto
Main article: mailto
The URI scheme, as registered with the IANA, defines the mailto: scheme for SMTP email addresses. Though its use is not strictly defined, URLs of this form are intended to be used to open the new message window of the user's mail client when the URL is activated, with the address as defined by the URL in the To: field.[58][59] Many clients also support query string parameters for the other email fields, such as its subject line or carbon copy recipients.[60]

Types
Web-based email
Main article: Webmail
Many email providers have a web-based email client (e.g. AOL Mail, Gmail, Outlook.com and Yahoo! Mail). This allows users to log into the email account by using any compatible web browser to send and receive their email. Mail is typically not downloaded to the web client, so can't be read without a current Internet connection.

POP3 email servers
The Post Office Protocol 3 (POP3) is a mail access protocol used by a client application to read messages from the mail server. Received messages are often deleted from the server. POP supports simple download-and-delete requirements for access to remote mailboxes (termed maildrop in the POP RFC's).[61]POP3 allows you to download email messages on your local computer and read them even when you are offline.[62][63]

IMAP email servers
The Internet Message Access Protocol (IMAP) provides features to manage a mailbox from multiple devices. Small portable devices like smartphones are increasingly used to check email while traveling and to make brief replies, larger devices with better keyboard access being used to reply at greater length. IMAP shows the headers of messages, the sender and the subject and the device needs to request to download specific messages. Usually, the mail is left in folders in the mail server.

MAPI email servers
Messaging Application Programming Interface (MAPI) is used by Microsoft Outlook to communicate to Microsoft Exchange Server - and to a range of other email server products such as Axigen Mail Server, Kerio Connect, Scalix, Zimbra, HP OpenMail, IBM Lotus Notes, Zarafa, and Bynari where vendors have added MAPI support to allow their products to be accessed directly via Outlook.

Uses

This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed. (November 2007) (Learn how and when to remove this template message)
Business and organizational use
Email has been widely accepted by businesses, governments and non-governmental organizations in the developed world, and it is one of the key parts of an 'e-revolution' in workplace communication (with the other key plank being widespread adoption of highspeed Internet). A sponsored 2010 study on workplace communication found 83% of U.S. knowledge workers felt email was critical to their success and productivity at work.[64]

It has some key benefits to business and other organizations, including:

Facilitating logistics
Much of the business world relies on communications between people who are not physically in the same building, area, or even country; setting up and attending an in-person meeting, telephone call, or conference call can be inconvenient, time-consuming, and costly. Email provides a method of exchanging information between two or more people with no set-up costs and that is generally far less expensive than a physical meeting or phone call.
Helping with synchronization
With real time communication by meetings or phone calls, participants must work on the same schedule, and each participant must spend the same amount of time in the meeting or call. Email allows asynchrony: each participant may control their schedule independently.
Reducing cost
Sending an email is much less expensive than sending postal mail, or long distance telephone calls, telex or telegrams.
Increasing speed
Much faster than most of the alternatives.
Creating a "written" record
Unlike a telephone or in-person conversation, email by its nature creates a detailed written record of the communication, the identity of the sender(s) and recipient(s) and the date and time the message was sent. In the event of a contract or legal dispute, saved emails can be used to prove that an individual was advised of certain issues, as each email has the date and time recorded on it.
Email marketing
Email marketing via "opt-in" is often successfully used to send special sales offerings and new product information.[65] Depending on the recipient's culture,[66] email sent without permission—such as an "opt-in"—is likely to be viewed as unwelcome "email spam".

Personal use
Personal computer
Many users access their personal emails from friends and family members using a personal computer in their house or apartment.

Mobile
Email has become used on smartphones and on all types of computers. Mobile "apps" for email increase accessibility to the medium for users who are out of their homes. While in the earliest years of email, users could only access email on desktop computers, in the 2010s, it is possible for users to check their email when they are away from home, whether they are across town or across the world. Alerts can also be sent to the smartphone or other devices to notify them immediately of new messages. This has given email the ability to be used for more frequent communication between users and allowed them to check their email and write messages throughout the day. As of 2011, there were approximately 1.4 billion email users worldwide and 50 billion non-spam emails that were sent daily.[59]

Individuals often check emails on smartphones for both personal and work-related messages. It was found that US adults check their email more than they browse the web or check their Facebook accounts, making email the most popular activity for users to do on their smartphones. 78% of the respondents in the study revealed that they check their email on their phone.[67] It was also found that 30% of consumers use only their smartphone to check their email, and 91% were likely to check their email at least once per day on their smartphone. However, the percentage of consumers using email on a smartphone ranges and differs dramatically across different countries. For example, in comparison to 75% of those consumers in the US who used it, only 17% in India did.[68]

Declining use among young people
As of 2010, the number of Americans visiting email web sites had fallen 6 percent after peaking in November 2009. For persons 12 to 17, the number was down 18 percent. Young people preferred instant messaging, texting and social media. Technology writer Matt Richtel said in The New York Times that email was like the VCR, vinyl records and film cameras—no longer cool and something older people do.[69][70]

A 2015 survey of Android users showed that persons 13 to 24 used messaging apps 3.5 times as much as those over 45, and were far less likely to use email.[71]

Issues

This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed. (October 2016) (Learn how and when to remove this template message)
Attachment size limitation
Main article: Email attachment
Email messages may have one or more attachments, which are additional files that are appended to the email. Typical attachments include Microsoft Word documents, PDF documents and scanned images of paper documents. In principle there is no technical restriction on the size or number of attachments, but in practice email clients, servers and Internet service providers implement various limitations on the size of files, or complete email - typically to 25MB or less.[72][73][74] Furthermore, due to technical reasons, attachment sizes as seen by these transport systems can differ to what the user sees,[75] which can be confusing to senders when trying to assess whether they can safely send a file by email. Where larger files need to be shared, various file hosting services are available and commonly used.[76][77]

Information overload
The ubiquity of email for knowledge workers and "white collar" employees has led to concerns that recipients face an "information overload" in dealing with increasing volumes of email.[78][79] With the growth in mobile devices, by default employees may also receive work-related emails outside of their working day. This can lead to increased stress, decreased satisfaction with work, and some observers even argue it could have a significant negative economic effect,[80] as efforts to read the many emails could reduce productivity.

Spam
Main article: Email spam
Email "spam" is unsolicited bulk email. The low cost of sending such email meant that, by 2003, up to 30% of total email traffic was spam,[81][82][83] and was threatening the usefulness of email as a practical tool. The US CAN-SPAM Act of 2003 and similar laws elsewhere[84] had some impact, and a number of effective anti-spam techniques now largely mitigate the impact of spam by filtering or rejecting it for most users,[85] but the volume sent is still very high—and increasingly consists not of advertisements for products, but malicious content or links.[86] In September 2017, for example, the proportion of spam to legitimate email rose to 59.56%.[87]

Malware
A range of malicious email types exist. These range from various types of email scams, including "social engineering" scams such as advance-fee scam "Nigerian letters", to phishing, email bombardment and email worms.

Email spoofing
Main article: Email spoofing
Email spoofing occurs when the email message header is designed to make the message appear to come from a known or trusted source. Email spam and phishing methods typically use spoofing to mislead the recipient about the true message origin. Email spoofing may be done as a prank, or as part of a criminal effort to defraud an individual or organization. An example of a potentially fraudulent email spoofing is if an individual creates an email that appears to be an invoice from a major company, and then sends it to one or more recipients. In some cases, these fraudulent emails incorporate the logo of the purported organization and even the email address may appear legitimate.

Email bombing
Main article: Email bomb
Email bombing is the intentional sending of large volumes of messages to a target address. The overloading of the target email address can render it unusable and can even cause the mail server to crash.

Privacy concerns
Main article: Email privacy
Today it can be important to distinguish between the Internet and internal email systems. Internet email may travel and be stored on networks and computers without the sender's or the recipient's control. During the transit time it is possible that third parties read or even modify the content. Internal mail systems, in which the information never leaves the organizational network, may be more secure, although information technology personnel and others whose function may involve monitoring or managing may be accessing the email of other employees.

Email privacy, without some security precautions, can be compromised because:

email messages are generally not encrypted.
email messages have to go through intermediate computers before reaching their destination, meaning it is relatively easy for others to intercept and read messages.
many Internet Service Providers (ISP) store copies of email messages on their mail servers before they are delivered. The backups of these can remain for up to several months on their server, despite deletion from the mailbox.
the "Received:"-fields and other information in the email can often identify the sender, preventing anonymous communication.
web bugs invisibly embedded in email content can alert the sender of any email whenever an email is read, or re-read, and from which IP address. It can also reveal whether an email was read on a smartphone or a PC, or Apple Mac device via the user agent string.
There are cryptography applications that can serve as a remedy to one or more of the above. For example, Virtual Private Networks or the Tor anonymity network can be used to encrypt traffic from the user machine to a safer network while GPG, PGP, SMEmail,[88] or S/MIME can be used for end-to-end message encryption, and SMTP STARTTLS or SMTP over Transport Layer Security/Secure Sockets Layer can be used to encrypt communications for a single mail hop between the SMTP client and the SMTP server.

Additionally, many mail user agents do not protect logins and passwords, making them easy to intercept by an attacker. Encrypted authentication schemes such as SASL prevent this. Finally, the attached files share many of the same hazards as those found in peer-to-peer filesharing. Attached files may contain trojans or viruses.

Legal contracts
Emails can now often be considered as binding contracts as well, so users must be careful about what they send through email correspondence.[89][90][91]

Flaming
Flaming occurs when a person sends a message (or many messages) with angry or antagonistic content. The term is derived from the use of the word incendiary to describe particularly heated email discussions. The ease and impersonality of email communications mean that the social norms that encourage civility in person or via telephone do not exist and civility may be forgotten.[92]

Email bankruptcy
Main article: Email bankruptcy
Also known as "email fatigue", email bankruptcy is when a user ignores a large number of email messages after falling behind in reading and answering them. The reason for falling behind is often due to information overload and a general sense there is so much information that it is not possible to read it all. As a solution, people occasionally send a "boilerplate" message explaining that their email inbox is full, and that they are in the process of clearing out all the messages. Harvard University law professor Lawrence Lessig is credited with coining this term, but he may only have popularized it.[93]

Internationalization
Originally Internet email was completely ASCII text-based. MIME now allows body content text and some header content text in international character sets, but other headers and email addresses using UTF-8, while standardized[94] have yet to be widely adopted.[2][95]

Further information: International email and Email address § Internationalization
Tracking of sent mail
The original SMTP mail service provides limited mechanisms for tracking a transmitted message, and none for verifying that it has been delivered or read. It requires that each mail server must either deliver it onward or return a failure notice (bounce message), but both software bugs and system failures can cause messages to be lost. To remedy this, the IETF introduced Delivery Status Notifications (delivery receipts) and Message Disposition Notifications (return receipts); however, these are not universally deployed in production.[nb 2]

Many ISPs now deliberately disable non-delivery reports (NDRs) and delivery receipts due to the activities of spammers:

Delivery Reports can be used to verify whether an address exists and if so, this indicates to a spammer that it is available to be spammed.
If the spammer uses a forged sender email address (email spoofing), then the innocent email address that was used can be flooded with NDRs from the many invalid email addresses the spammer may have attempted to mail. These NDRs then constitute spam from the ISP to the innocent user.
In the absence of standard methods, a range of system based around the use of web bugs have been developed. However, these are often seen as underhand or raising privacy concerns,[98][99] and only work with email clients that support rendering of HTML. Many mail clients now default to not showing "web content".[100] Webmail providers can also disrupt web bugs by pre-caching images.[101]

See also
Anonymous remailer
Anti-spam techniques
biff
Bounce message
Comparison of email clients
Dark Mail Alliance
Disposable email address
E-card
Electronic mailing list
Email art
Email authentication
Email digest
Email encryption
Email hosting service
Email storm
Email tracking
HTML email
Information overload
Internet fax
Internet mail standards
List of email subject abbreviations
MCI Mail
Netiquette
Posting style
Privacy-enhanced Electronic Mail
Push email
RSS
Telegraphy
Unicode and email
Usenet quoting
Webmail, Comparison of webmail providers
X-Originating-IP
X.400
Yerkish
Notes
 See Protocol Wars.
 A complete Message Tracking mechanism was also defined, but it never gained traction; see RFCs 3885[96] through 3888.[97]
References
 "RFC 5321 – Simple Mail Transfer Protocol". Network Working Group. Archived from the original on January 16, 2015. Retrieved January 19, 2015.
 "DataMail: World's first free linguistic email service supports eight India languages". Archived from the original on October 22, 2016.
 Brown, Ron (October 26, 1972). "Fax invades the mail market". New Scientist. Vol. 56 no. 817. London, England: New Scientist Ltd. pp. 218–221. Archived from the original on May 9, 2016.
 Luckett, Herbert P. (March 1973). "What's News: Electronic-mail delivery gets started". Popular Science. Vol. 202 no. 3. Harlan, Iowa: Bonnier Corporation. p. 85. Archived from the original on April 30, 2016.
 "email noun earlier than 1979". Oxford English Dictionary. October 25, 2012. Retrieved May 14, 2020.
 Ohlheiser, Abby (July 28, 2015). "Why the first use of the word 'e-mail' may be lost forever". Washington Post. Retrieved May 14, 2020.
 "Yahoo style guide". Styleguide.yahoo.com. Archived from the original on May 9, 2013. Retrieved January 9, 2014.
 "AP Removes Hyphen From 'Email' In Style Guide". Huffington Post. New York City: Huffington Post Media Group. March 18, 2011. Archived from the original on May 12, 2015.
 "RFC Editor Terms List". IETF. Archived from the original on December 28, 2013. This is suggested by the RFC Document Style Guide Archived 2015-04-24 at the Wayback Machine
 AskOxford Language Query team. "What is the correct way to spell 'e' words such as 'email', 'ecommerce', 'egovernment'?". FAQ. Oxford University Press. Archived from the original on July 1, 2008. Retrieved September 4, 2009. We recommend email, this is the common form
 "Reference.com". Dictionary.reference.com. Archived from the original on December 16, 2013. Retrieved January 9, 2014.
 Random House Unabridged Dictionary, 2006
 The American Heritage Dictionary of the English Language, Fourth Edition
 Princeton University WordNet 3.0
 The American Heritage Science Dictionary, 2002
 "Merriam-Webster Dictionary". Merriam-Webster. Archived from the original on May 12, 2014. Retrieved May 9, 2014.
 ""Email" or "e-mail"". English Language & Usage – Stack Exchange. August 25, 2010. Archived from the original on August 31, 2010. Retrieved September 26, 2010.
 Gerri Berendzen; Daniel Hunt. "AP changes e-mail to email". 15th National Conference of the American Copy Editors Society (2011, Phoenix). ACES. Archived from the original on March 22, 2011. Retrieved March 23, 2011.
 ""RFC Style Guide", Table of decisions on consistent use in RFC". Archived from the original on December 28, 2013. Retrieved January 9, 2014.
 "Excerpt from the FAQ list of the Usenet newsgroup alt.usage.english". Alt-usage-english.org. Archived from the original on April 3, 2012. Retrieved January 9, 2014.
 "Mail Objects". Simple Mail Transfer Protocol. IETF. sec. 2.3.1. doi:10.17487/RFC5321. RFC 5321. SMTP transports a mail object. A mail object contains an envelope and content.
 "Mail Objects". Simple Mail Transfer Protocol. IETF. sec. 2.3.1. doi:10.17487/RFC5321. RFC 5321. The SMTP content is sent in the SMTP DATA protocol unit, and has two parts: the header section and the body. If the content conforms to other contemporary standards, the header section is a collection of header fields, each consisting of a header name, a colon, and data, structured as in the message format specification
 Ray Tomlinson. "The First Network Email". Openmap.bbn.com. Retrieved October 5, 2019.
 "Retiring the NSFNET Backbone Service: Chronicling the End of an Era" Archived 2016-01-01 at the Wayback Machine, Susan R. Harris, Ph.D., and Elise Gerich, ConneXions, Vol. 10, No. 4, April 1996
 Leiner, Barry M.; Cerf, Vinton G.; Clark, David D.; Kahn, Robert E.; Kleinrock, Leonard; Lynch, Daniel C.; Postel, Jon; Roberts, Larry G.; Wolf, Stephen (1999). "A Brief History of the Internet". arXiv:cs/9901011. Bibcode:1999cs........1011L. Archived from the original on August 11, 2015.
 How E-mail Works. howstuffworks.com. 2008. Archived from the original on June 11, 2017.
 "MX Record Explanation" Archived 2015-01-17 at the Wayback Machine, it.cornell.edu
 "What is open relay?". WhatIs.com. Indiana University. July 19, 2004. Archived from the original on August 24, 2007. Retrieved April 7, 2008.
 Ch Seetha Ram (2010). Information Technology for Management. Deep & Deep Publications. p. 164. ISBN 978-81-8450-267-1.
 Hoffman, Paul (August 20, 2002). "Allowing Relaying in SMTP: A Series of Surveys". IMC Reports. Internet Mail Consortium. Archived from the original on January 18, 2007. Retrieved April 13, 2008.
 The Internet message format is also used for network news
 Simpson, Ken (October 3, 2008). "An update to the email standards". MailChannels Blog Entry. Archived from the original on October 6, 2008.
 J. Klensin (October 2008), "Mail Objects", Simple Mail Transfer Protocol, sec. 2.3.1., doi:10.17487/RFC5321, RFC 5321, SMTP transports a mail object. A mail object contains an envelope and content. ... The SMTP content is sent in the SMTP DATA protocol unit, and has two parts: the header section and the body.
 D. Crocker (July 2009), "Message Data", Internet Mail Architecture, sec. 4.1., doi:10.17487/RFC5598, RFC 5598, A message comprises a transit-handling envelope and the message content. The envelope contains information used by the MHS. The content is divided into a structured header and the body.
 P. Resnick, Ed. (October 2008). "RFC 5322, Internet Message Format". IETF. Archived from the original on February 22, 2015.
 Moore, K (November 1996). "MIME (Multipurpose Internet Mail Extensions) Part Three: Message Header Extensions for Non-ASCII Text". IETF. Archived from the original on January 14, 2012. Retrieved January 21, 2012.
 A Yang, Ed. (February 2012). "RFC 6532, Internationalized Email Headers". Ietf Request for Comments (RFC) Pages - Test. IETF. ISSN 2070-1721. Archived from the original on February 18, 2015.
 J. Yao, Ed., W. Mao, Ed. (February 2012). "RFC 6531, SMTP Extension for Internationalized Email Addresses". Ietf Request for Comments (RFC) Pages - Test. IETF. ISSN 2070-1721. Archived from the original on February 18, 2015.
 "Now, get your email address in Hindi - The Economic Times". The Economic Times. Archived from the original on August 28, 2016. Retrieved October 17, 2016.
 "RFC 5322, 3.6. Field Definitions". Tools.ietf.org. October 2008. Archived from the original on December 30, 2013. Retrieved January 9, 2014.
 "RFC 5322, 3.6.4. Identification Fields". Tools.ietf.org. October 2008. Archived from the original on December 30, 2013. Retrieved January 9, 2014.
 "RFC 5064". Tools.ietf.org. December 2007. Archived from the original on July 25, 2014. Retrieved January 9, 2014.
 Microsoft, Auto Response Suppress, 2010, Microsoft reference Archived 2011-04-07 at the Wayback Machine, 2010 Sep 22
 John Klensin (October 2008). "Trace Information". Simple Mail Transfer Protocol. IETF. sec. 4.4. doi:10.17487/RFC5321. RFC 5321.
 John Levine (January 14, 2012). "Trace headers". email message. IETF. Archived from the original on August 11, 2012. Retrieved January 16, 2012. there are many more trace fields than those two
 This extensible field is defined by RFC 7001, this also defines an IANA registry of Email Authentication Parameters.
 RFC 7208.
 "RFC6376". Retrieved January 28, 2020.
 Defined in RFC 3834, and updated by RFC 5436.
 RFC 5518.
 Craig Hunt (2002). TCP/IP Network Administration. O'Reilly Media. p. 70. ISBN 978-0-596-00297-8.
 "Email policies that prevent viruses". Archived from the original on May 12, 2007.
 "When posting to a RootsWeb mailing list..." Helpdesk.rootsweb.com. Archived from the original on February 19, 2014. Retrieved January 9, 2014.
 "...Plain text, 72 characters per line..." Openbsd.org. Archived from the original on February 8, 2014. Retrieved January 9, 2014.
 "How to Prevent the Winmail.dat File from Being Sent to Internet Users". Support.microsoft.com. July 2, 2010. Archived from the original on January 9, 2014. Retrieved January 9, 2014.
 In practice, some accepted messages may nowadays not be delivered to the recipient's InBox, but instead to a Spam or Junk folder which, especially in a corporate environment, may be inaccessible to the recipient
 "Free Email Providers in the Yahoo! Directory". dir.yahoo.com. Archived from the original on July 4, 2014.
 RFC 2368 section 3 : by Paul Hoffman in 1998 discusses operation of the "mailto" URL.
 Hansen, Derek; Smith, Marc A.; Heer, Jeffrey (2011). "E-Mail". In Barnett, George A (ed.). Encyclopedia of social networks. Thousand Oaks, Calif: Sage. p. 245. ISBN 9781412994170. OCLC 959670912.
 "Creating hyperlinks § E-mail links". MDN Web Docs. Retrieved September 30, 2019.
 Allen, David (2004). Windows to Linux. Prentice Hall. p. 192. ISBN 978-1423902454. Archived from the original on December 26, 2016.
 "Implementation and Operation". DISTRIBUTED ELECTRONIC MAIL MODELS IN IMAP4. sec. 4.5. doi:10.17487/RFC1733. RFC 1733.
 "Message Store (MS)". Internet Mail Architecture. sec. 4.2.2. doi:10.17487/RFC5598. RFC 5598.
 By Om Malik, GigaOm. "Is Email a Curse or a Boon? Archived 2010-12-04 at the Wayback Machine" September 22, 2010. Retrieved October 11, 2010.
 Martin, Brett A. S.; Van Durme, Joel; Raulas, Mika; Merisavo, Marko (2003). "E-mail Marketing: Exploratory Insights from Finland" (PDF). Journal of Advertising Research. 43 (3): 293–300. doi:10.1017/s0021849903030265. Archived (PDF) from the original on October 21, 2012.
 Lev, Amir (October 2, 2009). "Spam culture, part 1: China". Archived from the original on November 10, 2016.
 "Email Is Top Activity On Smartphones, Ahead Of Web Browsing & Facebook [Study]". March 28, 2013. Archived from the original on April 29, 2014.
 "The ultimate mobile email statistics overview". Archived from the original on July 11, 2014.
 Richtel, Matt (December 20, 2010). "E-Mail Gets an Instant Makeover". The New York Times. Retrieved April 4, 2018.
 Gustini, Ray (December 21, 2010). "Why Are Young People Abandoning Email?". The Atlantic. Retrieved April 4, 2018.
 Perez, Sarah (March 24, 2016). "Email is dying among mobile's youngest users". techcrunch.com. Retrieved April 4, 2018.
 "Setting Message Size Limits in Exchange 2010 and Exchange 2007" Archived 2013-02-12 at the Wayback Machine.
 "Google updates file size limits for Gmail and YouTube", geek.com Archived 2011-12-19 at the Wayback Machine.
 "Maximum attachment size", mail.google.com.
 "Exchange 2007: Attachment Size Increase,..." TechNet Magazine, Microsoft.com US. March 25, 2010. Archived from the original on August 25, 2016.
 "Send large files to other people" Archived 2016-08-07 at the Wayback Machine, Microsoft.com
 "8 ways to email large attachments" Archived 2016-07-02 at the Wayback Machine, Chris Hoffman, December 21, 2012, makeuseof.com
 Radicati, Sara. "Email Statistics Report, 2010" (PDF). Archived (PDF) from the original on September 1, 2011.
 Gross, Doug (October 20, 2010). "Happy Information Overload Day!". CNN. Archived from the original on October 23, 2015. Retrieved March 24, 2019.
 Stross, Randall (April 20, 2008). "Struggling to Evade the E-Mail Tsunami". The New York Times. Archived from the original on April 17, 2009. Retrieved May 1, 2010.
 "Seeing Spam? How To Take Care of Your Google Analytics Data". sitepronews.com. May 4, 2015. Archived from the original on November 7, 2017. Retrieved September 5, 2017.
 Rich Kawanagh. The top ten email spam list of 2005. ITVibe news, 2006, January 02, ITvibe.com Archived 2008-07-20 at the Wayback Machine
 How Microsoft is losing the war on spam Salon.com Archived 2008-06-29 at the Wayback Machine
 Spam Bill 2003 (PDF Archived 2006-09-11 at the Wayback Machine)
 "Google Says Its AI Catches 99.9 Percent of Gmail Spam" Archived 2016-09-16 at the Wayback Machine, Cade Metz, July 09 2015, wired.com
 "Spam and phishing in Q1 2016" Archived 2016-08-09 at the Wayback Machine, May 12, 2016, securelist.com
 "Kaspersky Lab Spam and Phishing report".
 SMEmail – A New Protocol for the Secure E-mail in Mobile Environments, Proceedings of the Australian Telecommunications Networks and Applications Conference (ATNAC'08), pp. 39–44, Adelaide, Australia, Dec. 2008.
 "When Email Exchanges Become Binding Contracts".
 "Is an Email Legally Binding: Everything You Need to Know".
 Corfield, Gareth. "UK court ruling says email signature blocks can sign binding contracts". The Register. Retrieved December 6, 2019.
 S. Kiesler; D. Zubrow; A.M. Moses; V. Geller (1985). "Affect in computer-mediated communication: an experiment in synchronous terminal-to-terminal discussion". Human-Computer Interaction. 1: 77–104. doi:10.1207/s15327051hci0101_3.
 Barrett, Grant (December 23, 2007). "All We Are Saying". The New York Times. Archived from the original on April 17, 2009. Retrieved December 24, 2007.
 "Internationalized Domain Names (IDNs) | Registry.In". registry.in. Archived from the original on May 13, 2016. Retrieved October 17, 2016.
 "Made In India 'Datamail' Empowers Russia With Email Address In Russian Language - Digital Conqueror". December 7, 2016. Archived from the original on March 5, 2017.
 RFC 3885, SMTP Service Extension for Message Tracking
 RFC 3888, Message Tracking Model and Requirements
 Amy Harmon (November 22, 2000). "Software That Tracks E-Mail Is Raising Privacy Concerns". The New York Times. Retrieved January 13, 2012.
 "About.com". Email.about.com. December 19, 2013. Archived from the original on August 27, 2016. Retrieved January 9, 2014.
 "Outlook: Web Bugs & Blocked HTML Images" Archived 2015-02-18 at the Wayback Machine, slipstick.com
 "Gmail blows up e-mail marketing..." Archived 2017-06-07 at the Wayback Machine, Ron Amadeo, Dec 13 2013, Ars Technica
Further reading
Cemil Betanov, Introduction to X.400, Artech House, ISBN 0-89006-597-7.
Marsha Egan, "Inbox Detox and The Habit of Email Excellence", Acanthus Publishing ISBN 978-0-9815589-8-1
Lawrence Hughes, Internet e-mail Protocols, Standards and Implementation, Artech House Publishers, ISBN 0-89006-939-5.
Kevin Johnson, Internet Email Protocols: A Developer's Guide, Addison-Wesley Professional, ISBN 0-201-43288-9.
Pete Loshin, Essential Email Standards: RFCs and Protocols Made Practical, John Wiley & Sons, ISBN 0-471-34597-0.
Partridge, Craig (April–June 2008). "The Technical Development of Internet Email" (PDF). IEEE Annals of the History of Computing. 30 (2): 3–29. doi:10.1109/mahc.2008.32. ISSN 1934-1547. Archived from the original (PDF) on June 2, 2016.
Sara Radicati, Electronic Mail: An Introduction to the X.400 Message Handling Standards, Mcgraw-Hill, ISBN 0-07-051104-7.
John Rhoton, Programmer's Guide to Internet Mail: SMTP, POP, IMAP, and LDAP, Elsevier, ISBN 1-55558-212-5.
John Rhoton, X.400 and SMTP: Battle of the E-mail Protocols, Elsevier, ISBN 1-55558-165-X.
David Wood, Programming Internet Mail, O'Reilly, ISBN 1-56592-479-7.
External links
	Look up email or outbox in Wiktionary, the free dictionary.
IANA's list of standard header fields
The History of Email is Dave Crocker's attempt at capturing the sequence of 'significant' occurrences in the evolution of email; a collaborative effort that also cites this page.
The History of Electronic Mail is a personal memoir by the implementer of an early email system
A Look at the Origins of Network Email is a short, yet vivid recap of the key historical facts
Business E-Mail Compromise - An Emerging Global Threat, FBI
vte
Computer-mediated communication
vte
Email clients
Authority control Edit this at Wikidata	
GND: 4191427-2LCCN: sh85042347NARA: 10636085NDL: 00576450
Categories: EmailInternet terminologyElectronic documentsHistory of the InternetComputer-related introductions in 1971
Navigation menu
Not logged inTalkContributionsCreate accountLog in
ArticleTalk
ReadView sourceView historySearch
Search Wikipedia
Main page
Contents
Current events
Random article
About Wikipedia
Contact us
Donate
Contribute
Help
Learn to edit
Community portal
Recent changes
Upload file
Tools
What links here
Related changes
Special pages
Permanent link
Page information
Cite this page
Wikidata item
Print/export
Download as PDF
Printable version
In other projects
Wikimedia Commons

Languages
বাংলা
ગુજરાતી
हिन्दी
ಕನ್ನಡ
മലയാളം
मराठी
தமிழ்
తెలుగు
اردو
130 more
Edit links
This page was last edited on 14 October 2020, at 14:46 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.
Privacy policyAbout WikipediaDisclaimersContact WikipediaMobile viewDevelopersStatisticsCookie statementWikimedia FoundationPowered by MediaWiki

 '''

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",str1)
print(email)