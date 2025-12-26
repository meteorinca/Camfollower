# 🖋️ ScribeCam

**Turn text into mechanical cam profiles.**

ScribeCam is a minimalist tool that generates mechanical cam profiles from text input. It visualizes the mechanism using a 2D simulation where a cam drives a follower to "write" the input characters.

## 🛠️ Tech Stack

*   **Frontend:** React (Vite) + Framer Motion (Animation)
*   **Backend:** Firebase Cloud Functions (Python 3.11)
*   **Database:** Firestore (Job tracking)
*   **Storage:** Firebase Storage (STL/CSV export)
*   **Language:** Python (Geometry Engine), JavaScript (UI)

## 🚀 Setup & Installation

### Prerequisites
*   Node.js (v18+)
*   Python (v3.11+)
*   Firebase CLI

### 1. Backend Setup (Python Functions)

Navigate to the functions directory and install dependencies:

```bash
cd functions
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

To run the validation script locally (generates test plots):

```bash
python validate_cam.py
```

### 2. Frontend Setup (React)

*Currently in development.*

```bash
cd frontend
npm install
npm run dev
```

## 🏗️ How it Works

1.  **Input:** User enters a character (e.g., "A").
2.  **Geometry Engine (Python):** 
    *   Maps the character to a path of (x,y) coordinates.
    *   Calculates the Inverse Kinematics (IK) to determine the necessary Cam Radius at every degree of rotation (0-360°) to push the follower to the correct height.
3.  **Visualization:** The React frontend receives the array of radii and uses Framer Motion to animate the rotating cam and the translating follower.

## 🧪 Testing

We include a `validate_cam.py` script to test the geometry engine without the full web stack.

*   **Circle Test:** Generates a constant radius profile.
*   **Line Test:** Generates a simple bump profile (simulating the number "1").

## ⚠️ Current Limitations (MVP)

*   Supports single character input (0-9).
*   2D Preview only (3D STL export planned).
*   Simplified kinematic model (vertical follower).

## 📄 License
MIT
