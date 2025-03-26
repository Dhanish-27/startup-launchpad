let counters = {
    startup: 0,
    elearn: 0,
    student: 0,
    mentor: 0,
    intern: 0,
college:0
};

let lastDate = getFormattedTimestamp(); // Initialize with the current date

// Function to get the formatted timestamp
function getFormattedTimestamp() {
    const now = new Date();
    const day = String(now.getDate()).padStart(2, '0');
    const month = String(now.getMonth() + 1).padStart(2, '0'); // Months are zero-based
    const year = now.getFullYear();

    return `${day}${month}${year}`; // Format: DDMMYYYY
}

// Function to generate a unique password
function generateUniquePassword(length) {
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+[]{}|;:,.<>?';
  let password = '';

  // Generate a random password
  for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * characters.length);
      password += characters[randomIndex];
  }

  // Append a unique identifier (e.g., timestamp)
  const timestamp = Date.now().toString(36); // Converts timestamp to base-36 string
  password += timestamp;

  return password;
}

// Generic function to update entry counters
function addEntry(category) {
    const currentDate = getFormattedTimestamp();

    // Check if the date has changed or the counter has reached its limit
    if (lastDate !== currentDate || counters[category] === 9999) {
        counters[category] = 0; // Reset the counter
        lastDate = currentDate; // Update the last date
    } else {
        counters[category]++; // Increment the counter
    }

    console.log(`Category: ${category}, Date: ${currentDate}, Counter: ${counters[category]}`);
}

// Usage functions for specific categories
function addEntrystart() {
    addEntry('startup');
}

function addEntrystudent() {
    addEntry('student');
}

function addEntryelearn() {
    addEntry('elearn');
}

function addEntrymentor() {
    addEntry('mentor');
}

function addEntryintern() {
  addEntry('intern');
}

function addEntrycollege() {
    addEntry('college');
}


async function startup_registration(event) {
    event.preventDefault()
    initialpart = "SR"
    secondpart = getFormattedTimestamp()
    addEntrystart()
    thirdpart = counters.startup
    user_id = initialpart+secondpart+thirdpart
    const formd = new FormData()
    formd.append('user_id',user_id)
    formd.append('startup_Name',document.getElementById('startup_Name').value)
    formd.append('founder_Name' ,document.getElementById('founder_Name').value)
    formd.append('founded_date',document.getElementById('founded_date').value)
    formd.append('contact_email',document.getElementById('contact_email').value)
    formd.append('contact_phonenumber',document.getElementById('contact_phonenumber').value)
    formd.append('sector',document.getElementById('sector').value)
    formd.append('company_stage',document.getElementById('company_stage').value)
    formd.append('employee_count',document.getElementById('employee_count').value)
    formd.append('Funding_Received',document.getElementById('Funding_Received').value)
    formd.append('Key_technology',document.getElementById('Key_technology').value)
    formd.append('Address_line_1',document.getElementById('Address_line_1').value)
    formd.append('Area',document.getElementById('Area').value)
    formd.append('city',document.getElementById('city').value)
    formd.append('state',document.getElementById('state').value)
    formd.append('zipcode', document.getElementById('zipcode').value)
    formd.append('Focus_area',document.getElementById('Focus_area').value)
    formd.append('Funding_duration',document.getElementById('Funding_duration').value)
    formd.append('Linkedin_link',document.getElementById('Linkedin_link').value)
    formd.append('Github_link',document.getElementById('Github_link').value)
    formd.append('Pitch_deck_link',document.getElementById('Pitch_deck_link').value)
    formd.append('reason',document.getElementById('reason').value)
    formd.append('password',generateUniquePassword(16))
    url = `http://127.0.0.1:8000/register_startup/`;
    try{
      response = await fetch(url,{
        method:"POST",
        body:formd
      })
      if(response.ok){
        alert('successfully registered')
      }
      else{
        alert('try again')
      }  
    }
    catch(error){
        console.log(error)
    }
    
}

    async function Mentor_registration(event) {
        event.preventDefault()
    initialpart = "MR"
    secondpart = getFormattedTimestamp()
    addEntrymentor()
    thirdpart = counters.mentor
    user_id = initialpart + secondpart + thirdpart
    const formd = new FormData()
    formd.append('user_id',user_id) 
    formd.append('Mentor_Name',document.getElementById('Mentor_Name').value)
    formd.append('contact_email', document.getElementById('contact_email').value)
    formd.append('contact_phonenumber',document.getElementById('contact_phonenumber').value)
    formd.append('Expertise',document.getElementById('Expertise').value)
    formd.append('Job_title',document.getElementById('Job_title').value)
    formd.append('Company_organisation',document.getElementById('Company_organisation').value)
    formd.append('Year_of_experience',document.getElementById('Year_of_experience').value)
    formd.append('Address_line_1',document.getElementById('Address_line_1').value)
    formd.append('Area',document.getElementById('Area').value)
    formd.append('city',document.getElementById('city').value)
    formd.append('state',document.getElementById('state').value)
    formd.append('zipcode',document.getElementById('zipcode').value)
    formd.append('Focus_area',document.getElementById('Focus_area').value)
    formd.append('Available_days',document.getElementById('Available_days').value)
    formd.append('Linkedin_link',document.getElementById('Linkedin_link').value)
    formd.append('Github_link',document.getElementById('Github_link').value)
    formd.append('resume_link',document.getElementById('resume_link').value)
    formd.append('Short_bio',document.getElementById('Short_bio').value)
    formd.append('password',generateUniquePassword(16))
    url = `http://127.0.0.1:8000/register_mentor/`;
    try{
        response = await fetch(url,{
          method:"POST",
          body:formd
        })
        if(response.ok){
          alert('successfully registered')
        }
        else{
          alert('try again')
        }  
      }
      catch(error){
          console.log(error)
      }
      
}

 async function elearning_registration(event){
    event.preventDefault()
  initialpart = "EL"
  secondpart = getFormattedTimestamp()
  addEntryelearn()
  thirdpart = counters.elearn
  user_id = initialpart + secondpart + thirdpart
  const formd = new FormData()
  formd.append('user_id',user_id) 
  formd.append('student_Name',document.getElementById('student_Name').value)
  formd.append('age',document.getElementById('age').value)
  formd.append('student_dob',document.getElementById('student_dob').value)
  formd.append('contact_email',document.getElementById('contact_email').value)
   formd.append('contact_phonenumber',document.getElementById('contact_phonenumber').value)
   formd.append('College_name',document.getElementById('College_name').value)
   formd.append('Department',document.getElementById('Department').value)
   formd.append('Current_year',document.getElementById('Current_year').value)
   formd.append('Year_of_graduation',document.getElementById('Year_of_graduation').value)
   formd.append('student_skills',document.getElementById('student_skills').value)
   formd.append('Address_line_1',document.getElementById('Address_line_1').value)
    formd.append('Area',document.getElementById('Area').value)
    formd.append('city',document.getElementById('city').value)
    formd.append('state',document.getElementById('state').value)
    formd.append('zipcode',document.getElementById('zipcode').value)
    formd.append('Linkedin_link',document.getElementById('Linkedin_link').value)
    formd.append('Github_link',document.getElementById('Github_link').value)
    formd.append('Resume_link',document.getElementById('Resume_link').value)
    formd.append('password',generateUniquePassword(16))
    url = `http://127.0.0.1:8000/register_elearning/`;
    try{
        response = await fetch(url,{
          method:"POST",
          body:formd
        })
        if(response.ok){
          alert('successfully registered')
        }
        else{
          alert('try again')
        }  
      }
      catch(error){
          console.log(error)
      }
    
}

async function internshipregistration(event){
  event.preventDefault();
  initialpart = "IN"
  secondpart = getFormattedTimestamp()
  addEntryintern()  
  thirdpart = counters.intern
  user_id = initialpart + secondpart + thirdpart
  const formd = new FormData()
  formd.append('user_id',user_id)
  formd.append('student_Name',document.getElementById('studentname').value)
  formd.append('age',document.getElementById('studentage').value)
  formd.append('student_dob',document.getElementById('studentdob').value)
  formd.append('contact_email',document.getElementById('studentemail').value)
   formd.append('contact_phonenumber',document.getElementById('studentphone').value)
   formd.append('College_name',document.getElementById('studentclg').value)
   formd.append('Department',document.getElementById('studentdept').value)
   formd.append('Current_year',document.getElementById('studentcurrentyear').value)
   formd.append('Year_of_graduation',document.getElementById('studentgradyear').value)
   formd.append('student_skills',document.getElementById('studentskills').value)
   formd.append('Address_line_1',document.getElementById('address').value)
    formd.append('Area',document.getElementById('studentarea').value)
    formd.append('city',document.getElementById('studentcity').value)
    formd.append('state',document.getElementById('studentstate').value)
    formd.append('zipcode',document.getElementById('pincode').value)
    formd.append('domain',document.getElementById('domain').value)
    formd.append('duration',document.getElementById('duration').value)
    formd.append('Linkedin_link',document.getElementById('studentlp').value)
    formd.append('Github_link',document.getElementById('studentgp').value)
    formd.append('Resume_link',document.getElementById('resumeurl').value)
    formd.append('reason',document.getElementById('studentreason').value)
    formd.append('password',generateUniquePassword(16))
    url = `http://127.0.0.1:8000/register_internship/`;
    try{
        response = await fetch(url,{
          method:"POST",
          body:formd
        })
        if(response.ok){
          alert('successfully registered')
        }
        else{
          alert('try again')
        }  
      }
      catch(error){
          console.log(error)
      }
   
}
async function college_registration(event) {
  event.preventDefault();
  alert('trigger')
  initialpart = "CL"
    secondpart = getFormattedTimestamp()
    addEntrycollege()
    thirdpart = counters.college
    user_id = initialpart + secondpart + thirdpart
    const formd = new FormData()
    formd.append('user_id', user_id)
    formd.append('student_Name', document.getElementById('student_Name').value)
    formd.append('contact_email', document.getElementById('contact_email').value)
    formd.append('contact_phonenumber', document.getElementById('contact_phonenumber').value)
    formd.append('College_name', document.getElementById('College_name').value)
    formd.append('Address_line_1', document.getElementById('Address_line_1').value)
    formd.append('Area', document.getElementById('Area').value)
    formd.append('city', document.getElementById('city').value)
    formd.append('state', document.getElementById('state').value)
    formd.append('zipcode', document.getElementById('zipcode').value)
    formd.append('password', generateUniquePassword(16))
    alert('entered')
    url = `http://127.0.0.1:8000/register_college/`;
    try {
        response = await fetch(url, {
            method: "POST",
            body: formd
        })
        if (response.ok) {
            alert('successfully registered')
        }
        else {
            alert('try again')
        }
    }
    catch (error) {
        alert(error)
    }

}