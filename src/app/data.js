import React from "react";

const stripTypes = [
  {
    name: "hero",
    label: "Hero"
  },
  {
    name: "card",
    label: "Card"
  }
];

const stripExamples = [
  {
    type: "hero",
    name: "Hero 1",
    jsx: (
      <div className="row">
        <h1>Hero 1</h1>
        <p>
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptatem
          dolore tempore vero cumque quibusdam nobis vel mollitia repellendus
          expedita sit, deserunt explicabo aspernatur ipsa at est sed
          perferendis fugiat porro officia? Libero consectetur incidunt ad
          inventore, ut exercitationem, reprehenderit cupiditate laboriosam
          veritatis, laudantium minus velit unde perferendis ipsam earum quis!
        </p>
      </div>
    )
  },
  {
    type: "hero",
    name: "Hero 2",
    jsx: (
      <div className="row">
        <h1>Hero 2</h1>
        <p>
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptatem
          dolore tempore vero cumque quibusdam nobis vel mollitia repellendus
          expedita sit, deserunt explicabo aspernatur ipsa at est sed
          perferendis fugiat porro officia? Libero consectetur incidunt ad
          inventore, ut exercitationem, reprehenderit cupiditate laboriosam
          veritatis, laudantium minus velit unde perferendis ipsam earum quis!
        </p>
      </div>
    )
  },
  {
    type: "card",
    name: "Two cards",
    jsx: (
      <div className="row">
        <div className="col-6 p-card">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam
          </p>
        </div>
        <div className="col-6 p-card">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam
          </p>
        </div>
      </div>
    )
  },
  {
    type: "card",
    name: "Three cards",
    jsx: (
      <div className="row">
        <div className="col-4 p-card">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam
          </p>
        </div>
        <div className="col-4 p-card">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam
          </p>
        </div>
        <div className="col-4 p-card">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam
          </p>
        </div>
      </div>
    )
  }
];

export { stripTypes, stripExamples };
