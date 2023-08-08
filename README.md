# GraphQL with Python using Strawberry

### To run the API
From a terminal...
```bash
cd virtualenv
strawberry server schema
```
Then open a browser and navigate to: `http://0.0.0.0:8000/graphql`

### Example Queries

#### Get all users

```
{  
  users {
    id
    name
    avatarUrl
  }
}
```

#### Get all posts
```
{
  posts {
    id
    title
    likes
    createdBy {
      id
      name
    }
    createdUtc
  }
}
```

#### Get a specific user
```
{
  user(id: "c0a5be09-d7b2-421e-9a91-591016280bd5") {
    id
    name
    avatarUrl
  }
}
```

#### Get a specific user with posts
```
{
  userWithPosts(id: "c0a5be09-d7b2-421e-9a91-591016280bd5") {
    id
    name
    avatarUrl
    posts {
      id
      title
      likes
      createdUtc
    }
  }
}
```


### Introspective Queries

#### Get all types

```
query {
  __schema {
    queryType {
      fields {
        name
        type {
          kind
          ofType {
            kind
            name
          }
        }
      }
    }
  }
}
```

#### Get properties for a type
```
query {
  __type(name: "User") {
    kind
    name
    fields {
      name
      type {
        kind
        name
        description
      }
    }
  }
}
```

#### Get all types, fields, queries, mutations, etc.
```
query IntrospectionQuery {
  __schema {
    queryType {
      name
    }
    mutationType {
      name
    }
    subscriptionType {
      name
    }
    types {
      ...FullType
    }
    directives {
      name
      description
      locations
      args {
        ...InputValue
      }
    }
  }
}

fragment FullType on __Type {
  kind
  name
  description
  fields(includeDeprecated: true) {
    name
    description
    args {
      ...InputValue
    }
    type {
      ...TypeRef
    }
    isDeprecated
    deprecationReason
  }
  inputFields {
    ...InputValue
  }
  interfaces {
    ...TypeRef
  }
  enumValues(includeDeprecated: true) {
    name
    description
    isDeprecated
    deprecationReason
  }
  possibleTypes {
    ...TypeRef
  }
}

fragment InputValue on __InputValue {
  name
  description
  type {
    ...TypeRef
  }
  defaultValue
}

fragment TypeRef on __Type {
  kind
  name
  ofType {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
              }
            }
          }
        }
      }
    }
  }
}
```
