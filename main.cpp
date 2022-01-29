#include <SFML/Graphics.hpp>
#include <fstream>
#include <iostream>
#include <cstring>

//std::ifstream in("circle_coordonates.txt");

struct line
{
    sf::Vertex p1;
    sf::Vertex p2;
};

std::vector<sf::VertexArray> circles;
std::vector<sf::RectangleShape> symbols;
std::vector<line> lins;
std::vector<sf::Text> litere;

bool overflow;
int depth;
int realDepth;
float  circleCoordonates[6283][8];
char prop[255];
char letters[26];
sf::Font *font;

sf::RectangleShape neg;
sf::RectangleShape nega;
sf::RectangleShape con;
sf::RectangleShape dis;
sf::RectangleShape imp;
sf::RectangleShape equ;
sf::Text *letter;

void  setup()
{
    std::ifstream in("circle_coordonates_and_size.txt");
    for(int i=0;i<6284;i++)
    {
        in>>circleCoordonates[i][0]>>circleCoordonates[i][1];
        in>>circleCoordonates[i][2]>>circleCoordonates[i][3];
        in>>circleCoordonates[i][4]>>circleCoordonates[i][5];
        in>>circleCoordonates[i][6]>>circleCoordonates[i][7];
    }
    in.close();

    nega.setSize(sf::Vector2f(30.0f, 30.0f));
    con.setSize(sf::Vector2f(30.0f, 30.0f));
    dis.setSize(sf::Vector2f(30.0f, 30.0f));
    imp.setSize(sf::Vector2f(30.0f, 30.0f));
    equ.setSize(sf::Vector2f(30.0f, 30.0f));

    sf::Texture *tex;
    tex = new sf::Texture();
    tex->loadFromFile("negation.png");
    nega.setTexture(tex);
    tex = new sf::Texture();
    tex->loadFromFile("disjunction.png");
    dis.setTexture(tex);
    tex = new sf::Texture();
    tex->loadFromFile("conjunction.png");
    con.setTexture(tex);
    tex = new sf::Texture();
    tex->loadFromFile("implies.png");
    imp.setTexture(tex);
    tex = new sf::Texture();
    tex->loadFromFile("equivalence.png");
    equ.setTexture(tex);

    nega.setOrigin(nega.getGlobalBounds().width/2.0f, nega.getGlobalBounds().height / 2.0f);
    dis.setOrigin(dis.getGlobalBounds().width / 2.0f ,dis.getGlobalBounds().height / 2.0f);
    con.setOrigin(con.getGlobalBounds().width / 2.0f ,con.getGlobalBounds().height / 2.0f);
    imp.setOrigin(imp.getGlobalBounds().width / 2.0f ,imp.getGlobalBounds().height / 2.0f);
    equ.setOrigin(equ.getGlobalBounds().width / 2.0f ,equ.getGlobalBounds().height / 2.0f);

    depth = 0;
    realDepth = 0;
    overflow = false;

    std::ifstream pIn("prop_for_graphic.txt");
    pIn.get(prop,255);
    pIn.close();

    for (char i='A';i<='Z';i++)
    {
        letters[i] = i;
    }
    font = new sf::Font();
    font->loadFromFile("arial-unicode-ms.ttf");
}
void drawStruct(sf::RenderWindow &window, line l)
{
    sf::Vertex v[] = {l.p1,l.p2};
    window.draw(v,2,sf::Lines);
}
void drawScreen(sf::RenderWindow &window)
{
    for (int i=0; i<circles.size();i++)
    {
        window.draw(circles[i]);
    }
    for (int i=0; i<symbols.size();i++)
    {
        window.draw(symbols[i]);
    }
    for (int i=0; i<lins.size(); i++)
    {
        drawStruct(window, lins[i]);
    }
    for (int i=0; i<litere.size(); i++)
    {
        window.draw(litere[i]);
    }
}
sf::Vertex createVertex(float x, float y, float px, float py)
{
    return sf::Vertex(sf::Vector2f(x + px, y + py));
}
void  addPointsToCircle(sf::VertexArray& vertexes, int i, float px, float py)
{
    vertexes.append(createVertex(circleCoordonates[i][0], circleCoordonates[i][1], px, py));
    vertexes.append(createVertex(circleCoordonates[i][2], circleCoordonates[i][3], px, py));
    vertexes.append(createVertex(circleCoordonates[i][4], circleCoordonates[i][5], px, py));
    vertexes.append(createVertex(circleCoordonates[i][6], circleCoordonates[i][7], px, py));
}
sf::VertexArray drawCircle(sf::RenderWindow &window, float px, float py, sf::Drawable &sym)
{
    sf::VertexArray curve(sf::PrimitiveType::LineStrip, 25000);
    curve.clear();

    for (int i=0;i<6280;i++)
    {
        addPointsToCircle(curve, i, px, py);
        if(i==6279 || i%(circles.size() < 15 ? (100 * (circles.size()/2) + 100) : 1500) == 0)
        {
            window.clear();
            window.draw(sym);
            window.draw(curve);
            drawScreen(window);
            window.display();
        }
    }
    std::cout<<"Circle drwned at "<<px<<"x"<<py<<std::endl;
    return curve;
}
void addCircleWithSymbol(sf::RenderWindow &window, float px, float py, sf::RectangleShape &sym)
{
    std::cout<<"Depth is "<<depth<<std::endl;
    sym.setPosition(sf::Vector2f(px,py));
    circles.push_back(drawCircle(window,px,py,sym));
    symbols.push_back(sym);
}
void addCircleWithLetter(sf::RenderWindow &window, float px, float py, char a)
{
    std::cout<<"Depth is "<<depth<<std::endl;
    std::string st;
    st += a;
    sf::Text t(st, *font);
    t.setCharacterSize(40);
    t.setStyle(sf::Text::Bold);
    t.setOrigin(sf::Vector2f(t.getLocalBounds().left + t.getLocalBounds().width / 2.0f,t.getLocalBounds().top +  t.getLocalBounds().height / 2.0f));
    t.setPosition(sf::Vector2f(px,py));
    circles.push_back(drawCircle(window,px,py,t));
    litere.push_back(t);
}
line drawLine(sf::RenderWindow &window, float x1, float y1, float x2, float y2)
{
    sf::Vertex p1(sf::Vector2f(x1,y1));
    sf::Vertex p2(sf::Vector2f(x2,y2));
    line lin = {p1,p2};

    for (int i=1;i<=1000;i++)
    {
        sf::Vertex pp2 = sf::Vertex(sf::Vector2f(p1.position.x + ((p2.position.x-p1.position.x) * i / 1000.0f), p1.position.y + ((p2.position.y-p1.position.y) * i / 1000.0f)));
        lin.p2 = pp2;
        if(i==1000 || i%(circles.size() < 10 ? (25 * (circles.size()/2) + 100) : (225)) == 0)
        {
            window.clear();
            drawStruct(window,lin);
            drawScreen(window);
            window.display();
        }
    }
    lin.p2 = p2;
    return lin;
}
void addLine(sf::RenderWindow &window, float x1, float y1, float x2, float y2)
{
    lins.push_back(drawLine(window,x1,y1,x2,y2));
}

int x;
void drawSymbol(sf::RenderWindow &window,float px, float py ,sf::RectangleShape sym)
{
    addCircleWithSymbol(window, px, py ,sym);
    x++;
    if(realDepth > 3)
    {
        depth = 3;
        overflow = !overflow;
    }
    else
    {
        depth = realDepth;
        overflow = false;
    }
    if(sym.getTexture() == nega.getTexture())
    {
        addLine(window,px,py+30.0f,px,py+53.42f);
        if(prop[x] >= 'A' && prop[x] <= 'Z')
        {
            addCircleWithLetter(window,px,py+83.42f,prop[x]);
        }
        else if(prop[x] == 'n')
        {
            drawSymbol(window, px,py+83.42f,nega);
        }
        else if(prop[x] == 'c')
        {
            drawSymbol(window, px,py+83.42f,con);
        }
        else if(prop[x] == 'd')
        {
            drawSymbol(window, px,py+83.42f,dis);
        }
        else if(prop[x] == 'i')
        {
            drawSymbol(window, px,py+83.42f,imp);
        }
        else if(prop[x] == 'e')
        {
            drawSymbol(window, px,py+83.42f,equ);
        }
    }
    else
    {
        depth++;
        realDepth++;
        int circleMaximNumber = 1;
        for (int i=0;i<depth;i++)
        {
            circleMaximNumber *= 2;
        }
        float widthCircle = window.getSize().x / circleMaximNumber;
        std::cout<<"widthCircle = "<<widthCircle<<" ";
        float exWidthCircle = widthCircle * 2;
        std::cout<<"exWidthCircle = "<<exWidthCircle<<" ";
        std::cout<<"px/exwidthcircle = "<<px<<"/"<<exWidthCircle<<" = "<<int(px/exWidthCircle)<<std::endl;
        float pozX = int(px/exWidthCircle) * widthCircle * 2 + widthCircle / 2.0f;
        std::cout<<"pozX = "<<pozX<<std::endl;
        addLine(window, px-21.21f,py+21.21f,pozX+21.21,py+61.21f);

        if(prop[x] >= 'A' && prop[x] <= 'Z')
        {
            addCircleWithLetter(window,pozX,py+83.42,prop[x]);
        }
        else if(prop[x] == 'n')
        {
            drawSymbol(window, pozX,py+83.42f,nega);
        }
        else if(prop[x] == 'c')
        {
            drawSymbol(window, pozX,py+83.42f,con);
        }
        else if(prop[x] == 'd')
        {
            drawSymbol(window, pozX,py+83.42f,dis);
        }
        else if(prop[x] == 'i')
        {
            drawSymbol(window, pozX,py+83.42f,imp);
        }
        else if(prop[x] == 'e')
        {
            drawSymbol(window, pozX,py+83.42f,equ);
        }
        x++;
        pozX += widthCircle ;
        addLine(window, px+21.21f,py+21.21f,pozX-21.21f,py+61.21f);
        std::cout<<"pozX = "<<pozX<<std::endl;
        if(prop[x] >= 'A' && prop[x] <= 'Z')
        {
            addCircleWithLetter(window,pozX,py+83.42,prop[x]);
        }
        else if(prop[x] == 'n')
        {
            drawSymbol(window, pozX,py+83.42f,nega);
        }
        else if(prop[x] == 'c')
        {
            drawSymbol(window, pozX,py+83.42f,con);
        }
        else if(prop[x] == 'd')
        {
            drawSymbol(window, pozX,py+83.42f,dis);
        }
        else if(prop[x] == 'i')
        {
            drawSymbol(window, pozX,py+83.42f,imp);
        }
        else if(prop[x] == 'e')
        {
            drawSymbol(window, pozX,py+83.42f,equ);
        }
        realDepth--;
        depth--;
    }
}

int main()
{
    sf::RenderWindow window(sf::VideoMode(1920, 1000), "SFML works!");
    setup();

    if (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }
        if(prop[0] == 'n')
        {
            drawSymbol(window, window.getSize().x/2.0f, 60.0f, nega);
        }
        else if(prop[0] == 'c')
        {
            drawSymbol(window, window.getSize().x/2.0f, 60.0f, con);
        }
        else if(prop[0] == 'd')
        {
            drawSymbol(window, window.getSize().x/2.0f, 60.0f, dis);
        }
        else if(prop[0] == 'i')
        {
            drawSymbol(window, window.getSize().x/2.0f, 60.0f, imp);
        }
        else if(prop[0] == 'e')
        {
            drawSymbol(window, window.getSize().x/2.0f, 60.0f, equ);
        }
        while(1);
    window.display();
    }

    return 0;
}
