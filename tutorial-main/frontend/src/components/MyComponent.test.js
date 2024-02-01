import React from "react";
import { render } from "@testing-library/react";
import MyComponent from "./MyComponent";

test("renders learn react link", () => {
  const { getByText } = render(<MyComponent name="Learn React" />);
    const linkElement = getByText(/learn react/i); 
    expect(linkElement).toBeInTheDocument();
}
);
