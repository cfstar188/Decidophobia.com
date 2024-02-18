export function NavBar() {
  return (
    <nav style={{ display: "flex" }}>
      <div className="text-white">
        <a href="#">Home</a>
        <a href="#" style={{ textDecoration: "none" }}>
          Pages
        </a>
        <a href="#" style={{ textDecoration: "none" }}>
          Discussion Board{" "}
        </a>
        <a href="/table" style={{ textDecoration: "none" }}>
          Compare
        </a>
      </div>
      {"{"}% if request.user.is_authenticated %{"}"}
      <div style={{ marginLeft: "auto", display: "flex" }}>
        <p>
          Welcome, {"{"}
          {"{"} request.user.username {"}"}
          {"}"}!
        </p>
        <a
          style={{ margin: 0, marginLeft: 5, textDecoration: "none" }}
          href="{% url 'logout' %}"
        >
          Logout
        </a>
      </div>
      {"{"}% else %{"}"}
      <div style={{ marginLeft: "auto" }}>
        <a href="/login" style={{ textDecoration: "none" }}>
          Login/Signup
        </a>
      </div>
      {"{"}% endif %{"}"}
    </nav>
  );
}
