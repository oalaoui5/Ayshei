import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


# Load logo image
logo_image = Image.open("chatbot.png") 

# Display logo in sidebar
st.sidebar.image(logo_image, width=100) 

# Display logo and title in main area
st.image(logo_image, width=150)


#Welcome message
st.title("Welcome to Ayshei")
os.environ['GOOGLE_API_KEY'] = "AIzaSyCMbI0KWhS_hUU5ld0Lc-iMkYK8Nq1XWgs"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Set up the model
generation_config = {
  "temperature": 0.1,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [{"text": part} for part in [

  
#Accounts & Ads
"input: How do I create a personal account?"
"output: Absolutely! Creating a personal account is easy. Just head over to the Ayshei website and click the ‘Sign Up’ button. You'll need to provide your email address, create a password, and agree to the terms and conditions. Let me know if you need further assistance!"
"input: Can I have multiple accounts?"
"output: I understand wanting multiple accounts, but Ayshei's terms of service only allow one account per user. This helps maintain transparency and trust within our community. Is there a specific reason you'd like another account? Perhaps I can help find a solution within our policies."
"input: I forgot my password, what do I do?"
"output: No worries, forgetting passwords happens! On the sign-in page, just click the 'Forgot Password' link and enter your Ayshei account email. You'll get a password reset link sent straight to your inbox."
"input: How can I change my email address?"
"output: Sure thing! To change your email address, navigate to your profile settings. You'll find the option to update it there. Don't forget to verify your new email through the confirmation link we'll send you."
"input: Can I use my social media account to sign up?"
"output: Currently, Ayshei doesn't support signing up directly with social media accounts. But creating an account with your email is quick and easy! We're always exploring new options, so stay tuned for future updates."
"input: How do I add a profile picture?"
"output: Adding a profile picture personalizes your account. In your profile settings, you'll find a section to upload your picture. Make sure it's a clear image of yourself and aligns with our community guidelines."
"input: What are the benefits of having a business account?"
"output: Great question! Business accounts on Ayshei come with perks like a branded business page, user management tools, and access to membership plans with exclusive benefits. You can explore membership plans here: https://ayshei.com/?overlay=sign-up"
"input: How do I switch from a personal account to a business account?"
"output: Upgrading to a business account is a smooth process. Head to the 'Business' section on Ayshei and choose 'Connect' or 'Get Started'. Follow the instructions to verify your business details and trade license. If you need help, I'm here for you!"
"input: Can I list items for sale with a personal account?"
"output: Absolutely! Both personal and business accounts can list items for sale. However, business accounts offer additional features like a branded page, which can be beneficial for larger-scale selling."
"input: What types of ads can I create on Ayshei?"
"output: Ayshei offers a variety of ad formats to suit your needs: Offer, Trade, Auction, Giveaway, and Request. Choose the one that best fits your item and selling goals. Need help deciding which ad type is right for you?"
"input: Are there any restrictions on what I can sell?"
"output: Yes, we have community guidelines outlining prohibited items and content, typically including illegal goods, counterfeits, and offensive materials. Make sure to review the guidelines before posting your ad to ensure a safe and positive experience for everyone."
"input: How do I choose the right category for my ad?"
"output: When creating an ad, select the category and sub-category that best describe your item. This ensures your ad reaches the right audience. If you're unsure, I can help you find the most suitable category!"
"input: What makes a good ad description?"
"output: A compelling ad description is clear, concise, and informative. Highlight key features, condition, and relevant keywords for better search visibility. Need some tips for writing a great description? I'm happy to help!"
"input: How many photos can I add to my ad?"
"output: You can add multiple photos to showcase your item from different angles. The exact number may vary by category, but generally, you can add several images to give buyers a complete view."
"input: Can I edit my ad after it's published?"
"output: Definitely! Go to your 'Dashboard' and then 'My Ads' to edit your ad's description, price, or photos anytime. "
"input: How do I promote my ad for more visibility?"
"output: To boost your ad's visibility, you can opt to pay a fee during the creation process. This promotes your listing to a wider audience and potentially attracts more buyers. Let me know if you'd like to explore this option!"

  #Buying & Selling
"input: How do I contact a seller?"
"output: Contacting sellers is easy! Use the Ayshei messenger – just look for the chat icon on the item listing and start a conversation."
"input: Can I negotiate the price with the seller?"
"output: Absolutely! Negotiation is encouraged on Ayshei. Use the chat messenger's negotiation tool to make offers and counteroffers for a transparent buying experience."
"input: How do I make an offer on an item?"
"output: To make an offer, find the 'Make an Offer' option on the item listing page. Enter your desired price and any conditions you may have. The seller will then review your offer."
"input: What is the watchlist and how do I use it?"
"output: The watchlist is a handy way to save items for later. Just click the heart icon on the item page, and it's added to your watchlist, accessible from your profile dropdown."
"input: How do I know if a seller is trustworthy?"
"output: While Ayshei promotes trust and safety, it's always good to be cautious. Check the seller's profile, reviews, and ratings to get an idea of their reputation. Feel free to ask me any questions you might have!"
"input: What is the 'Fast Sale' filter?"
"output: The 'Fast Sale' filter helps you find items sellers want to sell quickly. These listings are likely to be active for a shorter time, so if you see something you like, act fast!"
"input: Can I buy an item immediately without making an offer?"
"output: If the seller has listed a fixed price, you can click 'Buy Now' and proceed to checkout without making an offer. It's that simple!"
"input: How do I pay for an item?"
"output: Ayshei offers various payment methods like cash, cryptocurrency, bank transfer, and credit/debit cards. The options will be listed on the item page with the seller's preferred methods."
"input: Is it safe to pay online through Ayshei?"
"output: Yes, Ayshei uses secure payment gateways and an escrow service to ensure safe online transactions. Your funds are held securely until you confirm receipt of the item."
"input: Can I pay in installments?"
"output: We're currently working on introducing installment plans and auto-payment systems through partnerships with banks. Stay tuned for updates on this exciting feature!"
"input: Where can I find my purchase history?"
"output: Your purchase history is readily available in the avatar/favicon dropdown menu under 'Purchase History'. You'll find details of your past purchases and payment information."
"input: Can I leave a review for a seller?"
"output: Absolutely! After completing a purchase, you can leave a review for the seller. This helps other buyers and builds trust within the Ayshei community. Your feedback is valuable!"
"input: What happens if I receive a damaged item?"
"output: If you receive a damaged item, contact the seller immediately via Ayshei messenger. Depending on their return policy, you may be eligible for a refund or replacement."
"input: What should I do if I have a dispute with a seller?"
"output: First, try to resolve the issue directly with the seller through clear communication. If unsuccessful, you can report the issue to Ayshei's support team for assistance."
"input: Can I cancel an order after it's been placed?"
"output: Order cancellation depends on the seller's policy and whether the item has shipped. Reach out to the seller as soon as possible to discuss options. I can help guide you through the process!"

  #Fraud & Safety
"input: How do I stay safe when buying online?"
"output: Staying safe is a top priority! Keep communication within Ayshei messenger, avoid sharing sensitive info, watch out for suspicious links, and verify payments before sending items. Check out our Online Safety Checklist for more tips!"
"input: What are some red flags to watch out for when buying online?"
"output: Be cautious of deals too good to be true, pressure to pay outside Ayshei, and requests for unnecessary personal info. Trust your gut and prioritize your safety. If something feels off, let me know!"
"input: What should I do if I suspect a scam?"
"output: If you suspect a scam, stop communication with the seller, report it to Ayshei immediately, and consider contacting local authorities if necessary. We take your safety seriously and will help in any way we can."
"input: How can I verify the authenticity of a product?"
"output: While Ayshei can't guarantee authenticity for all products, research the item and seller, ask for detailed photos and descriptions, and consider secure payment methods like escrow."
"input: What happens if I buy a fake item? "
"output: If you believe you've purchased a fake item, report it to our support team. We'll investigate and work to rectify the situation, which may involve a return and action against the seller."
"input: How do I report a suspicious ad or seller?"
"output: You can report suspicious activity using the flag icon next to the ad or on the seller's profile. Our team reviews reports and takes appropriate action to keep our platform safe."
"input: What are some safety tips for meeting in person?"
"output: Choose a public place, inform someone of your plans, and trust your instincts when meeting in person. Our Offline Safety Checklist offers more detailed guidance for a secure experience."
"input: Should I share my phone number or email address with other users?"
"output: You have control over your contact information. During ad creation, you can choose to hide your phone number and email and only share them with users you've messaged. It's up to you!"
"input: What is phishing and how can I avoid it?"
"output: Phishing is an attempt to steal information through deceptive emails or websites. Always double-check addresses and domain names, and avoid suspicious links. Ayshei will never ask for your password via email."
"input: How does Ayshei protect my personal information? "
"output: Ayshei employs industry-standard security measures, including secure servers and encryption protocols, to protect your data. We prioritize your privacy and data security."
"input: What should I do if I lose my phone or it gets stolen?"
"output: If you lose your phone, change your Ayshei password immediately and report it to your mobile service provider to prevent unauthorized access to your account."
"input: Can someone hack my Ayshei account?"
"output: While no platform is entirely hack-proof, Ayshei has security measures to protect your account. Using a strong password, being cautious of phishing, and keeping software updated minimizes risks."
"input: Is Ayshei responsible for transactions that happen outside of the platform?"
"output: Ayshei's responsibility is limited to activities within the platform. Agreements or payments outside of Ayshei are beyond our control, and you'd need to seek legal recourse if issues arise."

  #Motors
"input: Can I sell any type of vehicle on Ayshei?"
"output: Yes, Ayshei's Motors section welcomes various vehicles – cars, motorcycles, boats, and even heavy equipment. What type of vehicle are you looking to sell?"
"input: How do I list my car for sale?"
"output: Listing your car is easy! In the Motors section, click 'Sell Your Car' and provide details like make, model, year, mileage, condition, and photos. Then, set your asking price and you're good to go!"
"input: What is the 'Verified' badge on some car listings?"
"output: The 'Verified' badge indicates the car has been inspected by one of our partner agencies, giving buyers extra confidence in the listing's accuracy."
"input: How do I get my car verified? "
"output: During ad creation, you can request car verification for a fee. This involves an inspection by a partner agency, and if your car meets the criteria, it earns the 'Verified' badge."
"input: What does the car verification process entail? "
"output: The verification process typically includes a thorough inspection of the car's exterior, interior, engine, and components, along with verification of documentation and history. It ensures transparency and builds trust with potential buyers."
"input: Can I book a test drive before buying a car? "
"output: Test drive availability depends on the seller. Reach out to them through the Ayshei messenger to inquire about a test drive and get a feel for the car before making a decision."
"input: What if the car's condition is not as described in the ad? "
"output: If you find significant discrepancies, you're entitled to a full refund. We take misrepresentation seriously and will penalize sellers who violate our guidelines. Your satisfaction is important to us!"
"input: Does the car come with a warranty? "
"output: The warranty would be the remaining portion of the manufacturer's original warranty, if still valid. Ayshei itself doesn't provide warranties on vehicles."
"input: Is car insurance mandatory? "
"output: Car insurance is required in the UAE if the vehicle has a number plate registration. If you're buying a car without a plate, insurance is needed upon registration."
"input: How does the car transfer process work? "
"output: Both buyer and seller need to visit the official registration authority with Emirates ID, driver's license, and passport for the legal transfer of the car. It's a straightforward process."
"input: Can I sell my car's license plate separately? "
"output: Yes, you can sell your car's license plate separately, either mentioning it in the car's ad or creating a separate ad in the Motors category specifically for the license plate."
"input: Does Ayshei offer financing options for car purchases? "
"output: We're actively working on car financing options with partner banks, including installment plans and auto-payment systems. Stay tuned for these convenient features!"
"input: What documents do I need to sell my car on Ayshei?"
"output: To sell your car, you'll need the car's registration documents, your Emirates ID, and any service records or inspection reports. Having these ready makes the process smoother."
"input: What happens if I lose the car keys after buying it? "
"output: If you lose the keys, you'll likely need to contact a locksmith or the car dealership for replacements. As the new owner, this cost would be your responsibility."
#Properties
"input: What types of properties can I list on Ayshei?"
"output: Ayshei's Properties section covers a wide range – apartments, villas, townhouses, commercial spaces, and land. What type of property are you considering listing?"
"input: How do I list my property for sale or rent?"
"output: Listing your property is simple! Go to the Properties section and choose 'Sell' or 'Rent'. Provide details, photos, and set your asking price or rental rate."
"input: What is the 'Verified' badge on some property listings?"
"output: The 'Verified' badge indicates the property and its details have been inspected and confirmed as legitimate by one of our partner agencies, providing assurance to potential buyers or renters."
"input: How do I get my property verified?"
"output: During ad creation, apply for property verification for a fee. This involves a form and inspection by a partner agency. If successful, your listing gets the 'Verified' badge."
"input: What documents do I need to provide for property verification? "
"output: Required documents may vary, but typically include the title deed, property photos, and any agreements between seller and agent. Having these prepared streamlines the process."
"input: Can I list a property under construction?"
"output: Yes, you can list properties under construction, but clearly indicate the status and provide accurate information on the expected completion date and any risks involved."
"input: Can I schedule property viewings through Ayshei?"
"output: Absolutely! Ayshei makes scheduling viewings easy. Communicate directly with potential buyers/renters through the platform's messaging system and arrange viewings at your convenience."
"input: What if I'm not happy with the condition of the property after moving in? "
"output: Contact the seller/landlord immediately if you discover discrepancies. Depending on your agreement, you may be entitled to repairs, compensation, or lease termination. We're here to help if needed!"
"input: Does Ayshei offer any legal assistance with property transactions?"
"output: While Ayshei provides a platform for listings and communication, seeking professional legal advice for complex property transactions or contractual matters is recommended."
"input: How can I ensure the safety of my documents during the verification process?"
"output: We prioritize document security. All documents submitted are handled through secure servers and kept confidential, so you can have peace of mind."
"input: Can I list a property on behalf of someone else?"
"output: Yes, you can list for others with their permission and necessary documentation. Just make sure everything is in order before creating the ad."
"input: What happens if there's a dispute between me and the seller/landlord? "
"output: Try resolving disputes amicably first. If unsuccessful, consider mediation or legal counsel for assistance. Ayshei promotes open communication and a positive experience for all users."

  #Shipping & Tracking
"input: What shipping options are available on Ayshei?"
"output: We currently partner with Transguard for reliable shipping within the UAE. They offer efficient and secure delivery services for your convenience."
"input: How do I choose a shipping method?"
"output: As a seller, you decide if you'll offer shipping and select the preferred methods during ad creation. Buyers will see available options during checkout."
"input: How much does shipping cost?"
"output: Shipping costs depend on item weight, size, and distance between buyer and seller. The estimated cost is shown during checkout for transparency."
"input: Is there a way to get free shipping?"
"output: Some sellers offer free shipping for orders above a certain value. Check the item listing or your wishlist to see if free shipping is available for your desired item."
"input: How does the shipping process work?"
"output: Once the buyer selects shipping and provides their address, the seller prepares the item for Transguard pickup. The buyer gets a tracking number to follow the shipment's progress."
"input: Can I track my package?"
"output: Absolutely! You'll receive a tracking number in your email notification, which you can use on the Transguard website or app to stay updated on your package's journey."
"input: What happens if my package is lost or stolen? "
"output: In rare cases of loss or theft, Transguard is liable. Ayshei will assist you in getting a refund or rescheduling the delivery. Your satisfaction is our priority."
"input: What if I receive the wrong item? "
"output: Contact the seller immediately if you receive the wrong item. You're entitled to a full refund, and the seller may face penalties for policy violations. We ensure fairness for all our users."
"input: How long does shipping usually take?"
"output: Delivery times vary based on distance and shipping method. Generally, expect delivery within a few business days within the UAE. You can always track your package for real-time updates."
"input: Can I change my shipping address after placing an order?"
"output: Contact the seller ASAP if you need to change your address. If the item hasn't shipped, they may be able to update it for you. We understand that things can change!"
"input: What if I'm not available to receive the package?"
"output: No problem! Contact Transguard directly using the tracking number to reschedule delivery for a time that suits you best. They're flexible and accommodating."
"input: Can I pick up the item directly from the seller? "
"output: Local pickup depends on the seller's preference and whether they've enabled this option. Check the item listing or ask the seller directly."
"input: Does Ayshei offer international shipping?"
"output: Currently, our shipping is within the UAE, but we're exploring international shipping options for the future. Stay tuned for updates as we expand our services!"

  #Returns & Refunds
"input: What is Ayshei's return policy?"
"output: The return policy is set by each seller and outlined in their item listings. It details whether returns are accepted, the timeframe, and who covers return shipping costs."
"input: How do I initiate a return?"
"output: If the seller accepts returns, contact them through Ayshei messenger explaining the reason for return and follow their instructions."
"input: Who pays for return shipping?"
"output: Responsibility for return shipping costs depends on the seller's policy. It could be the buyer, seller, or shared, depending on the reason for return."
"input: How long does it take to receive a refund?"
"output: Once the seller approves the return, expect a refund to your Ayshei wallet within 2-5 working days. We process refunds promptly to ensure a smooth experience."
"input: Can I get a refund if I change my mind about a purchase?"
"output: Refund eligibility for change of mind depends on the seller's return policy. Some may accept returns in such cases, while others may not. Always review the return policy before making a purchase!"
"input: What if the item I receive is not as described? "
"output: If the item significantly differs from its description, you're entitled to a full refund. Contact the seller and Ayshei's support for assistance. We're here to ensure you have a positive buying experience."
"input: Can I return an item if it's damaged during shipping?"
"output: If an item arrives damaged, contact the seller and Transguard (shipping company) immediately to file a claim. You may be eligible for a refund or replacement depending on the situation."
"input: What if the seller refuses to accept my return? "
"output: If you have a valid reason for return and the seller is uncooperative, contact Ayshei support. We'll investigate and help mediate a resolution. Fairness is important to us!"
"input: Can I exchange an item instead of getting a refund?"
"output: Exchange possibilities depend on the seller's policies and inventory. Reach out to the seller to inquire about exchange options for the item you purchased."
"input: What happens if I used a coupon or discount code on my purchase?"
"output: The refund amount typically reflects the final price paid after the discount. You'll receive the amount you actually spent on the item."
"input: Can I cancel an offer I made on an item?"
"output: Yes, you can cancel an offer as long as the seller hasn't accepted it yet. There are no penalties for changing your mind."
"input: What happens if a seller claims I didn't return the item?"
"output: Use a trackable shipping method for returns to have proof of delivery and resolve any disputes. This protects both you and the seller."
#Fees & Billing
"input: What payment methods does Ayshei accept?"
"output: We offer a range of payment options for your convenience, including Visa/Mastercard, Tabby Pay, and Cryptocurrency."
"input: How do online payments work on Ayshei?"
"output: Online payments are held securely in our escrow account until the buyer confirms item receipt, ensuring a safe and reliable transaction for both parties."
"input: Are there any fees for using online payment methods?"
"output: Yes, there's a small fee on sales made through credit/debit cards (2.9% + 1 AED) and cryptocurrency (2% + 1 AED), plus the applicable 5% VAT."
"input: Are there any additional fees besides the sales fee?"
"output: There might be a shipping fee depending on the item and seller's preferences. The total cost, including any applicable fees, will always be displayed transparently before you finalize your purchase."
"input: Do I need to pay taxes on my purchases? "
"output: Yes, all purchases on Ayshei are subject to a 5% Value Added Tax (VAT) in accordance with UAE regulations."
"input: How can I view my billing history?"
"output: Your billing history with payments and fees is accessible through your profile dropdown menu under 'Purchase History'. You can easily keep track of your transactions."
"input: What is Ayshei's escrow service?"
"output: Escrow is a secure system where Ayshei holds the buyer's payment until they confirm item receipt. It protects both buyers and sellers and ensures a smooth transaction process."
"input: Can I get a loan through Ayshei?"
"output: We're planning to offer installment loan options via partner banks for larger purchases like cars or properties. These loans will be provided as wallet credits and become a negative balance upon use (coming soon)."
"input: How does Ayshei make money?"
"output: Our primary revenue comes from the small sales fee on transactions and potential future partnerships with banks for loan services."
"input: Do sellers have to pay any fees? "
"output: No, listing items on Ayshei is completely free for sellers. We only charge fees to buyers upon successful sale completion."
"input: What is Ayshei's policy on refunds for canceled orders?"
"output: For canceled orders before shipping, buyers receive a full refund within 2-5 working days. We aim to make the process as smooth as possible."
"input: How can I contact Ayshei if I have billing questions?"
"output: For any billing questions or assistance, call our customer support team at800-AYSHEI (800 297 434)"
"from 9 AM to 9 PM, Monday to Sunday."
"We're always happy to help!"
"input: Crypto"
"output: Ah, cryptocurrency! Are you interested in learning how crypto payments work on Ayshei, or perhaps you're wondering if you can accept crypto payments as a seller? Let me know how I can assist you further with your crypto-related questions!"

#Auctions 

"Input: What are the rules for participating in auctions on Ayshei"
"Output: To ensure a fair and transparent experience for all users, Ayshei has established the following rules for auctions: "
"* **Bidding**: All bids placed are considered binding contracts. Bidders are responsible for ensuring they have the financial means to complete the purchase if they win"
"* **Reserve Price: Sellers may set a reserve price, which is the minimum amount they are willing to accept for the item. The item will only be sold if the highest bid meets or exceeds the reserve price"
"* **Bid Increments**: Auctions will have specified bid increments to ensure fair bidding opportunities for all participants"
"* **Auction Ending**: The auction will end at the specified date and time. In the event of a last-minute bid, the auction may be extended to allow other bidders a chance to respond"
"* **Winning Bidder**: The user with the highest bid at the end of the auction and meeting the reserve price will win the item and be obligated to complete the purchase"
"* **Payment**: Payment for auction items follows the same process as regular purchases on Ayshei. The available payment methods will be determined by the seller and displayed on the auction page"
"* **Non-Payment**: Failure to complete the purchase after winning an auction may result in penalties, including account restrictions "
"We encourage all users to carefully review the auction details and rules before placing any bids. For any further questions or clarifications, please feel free to ask!"

  
"Input: How do auctions work on Ayshei?"
"Output: Auctions on Ayshei allow buyers to bid on items, with the highest bidder winning the item at the end of the auction period. Each auction will have specific details, such as a starting bid, bid increments, and a reserve price."
"Input: What is a reserve price?"
"Output: A reserve price is the minimum amount that a seller is willing to accept for an item. If the highest bid at the end of the auction doesn't reach the reserve price, the seller is not obligated to sell the item."
"Input: Can I set a maximum bid?"
"Output: Yes, you can! When placing a bid, you have the option to set a maximum bid. This means the system will automatically bid on your behalf up to your maximum limit, even if you're not actively participating in the bidding process."
"Input: What happens if two people place the same bid?"
"Output: If two users place the same bid, the bid that was placed first will take priority."
"Input: How do I know if I'm the highest bidder?"
"Output: You can easily track the current highest bid on the auction page. Additionally, you will receive notifications if you are outbid by another user."
"Input: What happens if I win the auction?"
"Output: If you are the highest bidder at the end of the auction and the reserve price is met, you will win the item and be obligated to complete the purchase."
"Input: Can I retract my bid?"
"Output: Generally, bids are considered binding contracts and cannot be retracted. However, there may be exceptional circumstances where bid retractions are considered. We recommend carefully reviewing the auction details and bidding responsibly."
"Input: How do I pay for an item I won in an auction?"
"Output: Payment for auction items follows the same process as regular purchases. You can choose from various payment methods such as cash, cryptocurrency, bank transfer, or credit/debit cards, depending on the seller's preferences."


# Call center 
"Input: What is the call center contact or help center or customer support ?"
"Output: Chat with US"
" Customer Enqueries** : support@ayshei.com "
" Or call us **800-AYSHEI**  from Mon - Sun from 9 AM to 9 PM"


]]


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": " AysheiGPT here. How can I make your experience smoother today?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Process and store Query and Response
def llm_function(query):
    response = model.generate_content(prompt_parts + [{"text": f"input: {query}"}])
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "user", "content": query})
    st.session_state.messages.append({"role": "assistant", "content": response.text})

# Accept user input
query = st.chat_input("What's up?")

# Calling the Function when Input is Provided
if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(query)
